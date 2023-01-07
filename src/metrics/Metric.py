from ..boxes.Treebank import Treebank
from ..boxes.Sentence import Sentence
from dataclasses import dataclass
from typing import List, Mapping, TypedDict, Callable
from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from ..util.core import find


@dataclass
class Result:
    sent_id: str
    lang_code: str
    value: float
    sent_id_eng: str = None
    reference_value: float = None
    offset_from_reference: float = None


@dataclass
class MetricParallelOutput:
    reference: List[Result]  # Result for reference treebank
    treebanks: Mapping[str, List[Result]]  # Results for other treebanks
    # Average for each treebank, as identified by language code
    treebank_averages: Mapping[str, float]
    reference_lang_code: str = None

    def __str__(self) -> str:
        return f"MetricParallelOutput - average values {self.treebank_averages} - reference {bool(self.reference)} - {len(self.treebanks)} treebanks"

    def to_pandas(self) -> pd.DataFrame:
        class Column(TypedDict):
            key: str
            getter: Callable[[str], float]

        def __build_finder(lang_code: str, value_field: str):
            def finder(sent_id: str):
                item = find(lambda r: r.sent_id_eng == sent_id,
                            self.treebanks[lang_code])
                if value_field == "value":
                    return item.value
                elif value_field == "reference_value":
                    return item.offset_from_reference
            return finder

        if self.reference_lang_code:
            row_labels = list(map(lambda r: r.sent_id_eng, self.reference))
            columns: List[Column] = [
                {
                    "key": f"{self.reference_lang_code} (reference)",
                    "getter": lambda sid: find(lambda r: r.sent_id == sid, self.reference).value
                },
                *[
                    {
                        "key": f"{lang_code}",
                        "getter": __build_finder(lang_code, "value")
                    } for lang_code in self.treebanks.keys()
                ],
                *[
                    {
                        "key": f"{lang_code} (offset from reference)",
                        "getter": __build_finder(lang_code, "reference_value")
                    } for lang_code in self.treebanks.keys()
                ]
            ]
            arr = np.zeros((len(row_labels), len(columns)), dtype=np.float32)
            for i, sent_id in enumerate(row_labels):
                for j, column in enumerate(columns):
                    try:
                        value = column["getter"](sent_id)
                        arr[i, j] = value
                    except AttributeError:
                        print("Item not found", sent_id, column["key"])

            return pd.DataFrame(arr, index=row_labels, columns=list(map(lambda c: c["key"], columns)))

        else:
            columns: List[Column] = [
                {
                    "key": f"{lang_code}",
                    "getter": __build_finder(lang_code, "value"),
                } for lang_code in self.treebanks.keys()
            ]
            sample_tb = list(self.treebanks.values())[0]
            row_labels = list(map(lambda r: r.sent_id_eng,
                              sample_tb))
            col_labels = list(map(lambda c: c["key"], columns))
            arr = np.zeros((len(row_labels), len(columns)), dtype=np.float32)
            for i, sent_id in enumerate(row_labels):
                for j, column in enumerate(columns):
                    try:
                        value = column["getter"](sent_id)
                        arr[i, j] = value
                    except AttributeError:
                        print("Item not found", sent_id, column["key"])
            df = pd.DataFrame(arr, index=row_labels, columns=col_labels)
            return df


class Metric(ABC):
    @abstractmethod
    def for_sentence(self, sentence: Sentence) -> float:
        pass

    def for_treebank(self, treebank: Treebank) -> List[Result]:
        results = []
        for sentence in treebank.sentences:
            value = self.for_sentence(sentence)
            results.append(Result(
                lang_code=treebank.lang_code,
                sent_id=sentence.sent_id,
                sent_id_eng=sentence.sent_id_eng,
                value=value
            ))
        return results

    def for_parellel_treebanks(self, treebanks: List[Treebank], reference_treebank: Treebank = None) -> MetricParallelOutput:
        """
        Compute metric for multiple treebanks. Results are grouped by sentence id. If reference
        treebank is provided, results for the other treebank are also reported as the difference
        from the reference.

        Args:
            treebanks (List[Treebank]): List of treebanks to compute metric for.
            reference_treebank (Treebank, optional): Reference for other treebank results. Defaults to None.

        Returns:
            output (MetricParallelOutput): Metric results for each treebank.
        """
        reference_results = None
        reference_values = None
        if reference_treebank:
            # If reference is provided, compute values for it
            reference_results = self.for_treebank(reference_treebank)
            reference_values = {
                result.sent_id_eng: result.value for result in reference_results}
        final = MetricParallelOutput(
            reference=reference_results, treebanks={}, treebank_averages={})
        if reference_values:
            # If reference is provided, record its average value in the result
            final.reference_lang_code = reference_treebank.lang_code
            final.treebank_averages[reference_treebank.lang_code] = sum(
                reference_values.values()) / len(reference_values.values())
        for treebank in treebanks:
            # Compute metric values for each treebank
            treebank_result = self.for_treebank(treebank)
            treebank_values = [result.value for result in treebank_result]
            if reference_values:
                # If reference is provided, compute offset from reference for each
                # result in each treebank
                for result in treebank_result:
                    result.reference_value = reference_values[result.sent_id_eng]
                    result.offset_from_reference = result.value - \
                        result.reference_value
            final.treebanks[treebank.lang_code] = treebank_result
            final.treebank_averages[treebank.lang_code] = sum(
                treebank_values) / len(treebank_values)

        return final
