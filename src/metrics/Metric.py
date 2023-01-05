from ..boxes.Treebank import Treebank
from ..boxes.Sentence import Sentence
from dataclasses import dataclass
from typing import List, Mapping
from abc import ABC, abstractmethod


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

    def __str__(self) -> str:
        return f"MetricParallelOutput - average values {self.treebank_averages} - reference {bool(self.reference)} - {len(self.treebanks)} treebanks"


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
            reference_results = self.for_treebank(reference_treebank)
            reference_values = {
                result.sent_id: result.value for result in reference_results}
        final = MetricParallelOutput(
            reference=reference_results, treebanks={}, treebank_averages={})
        if reference_values:
            final.treebank_averages[reference_treebank.lang_code] = sum(
                reference_values.values()) / len(reference_values.values())
        for treebank in treebanks:
            treebank_result = self.for_treebank(treebank)
            treebank_values = [result.value for result in treebank_result]
            if reference_values:
                for result in treebank_result:
                    result.reference_value = reference_values[result.sent_id_eng]
                    result.offset_from_reference = result.value - \
                        result.reference_value
            final.treebanks[treebank.lang_code] = treebank_result
            final.treebank_averages[treebank.lang_code] = sum(
                treebank_values) / len(treebank_values)

        return final
