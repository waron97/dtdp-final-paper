from .Metric import TreebankLevelMetric
from ..boxes.Treebank import Treebank
from typing import Dict, MutableSet


class WordFormsPerLemma(TreebankLevelMetric):
    def compute(self, treebank: Treebank) -> float:
        forms: Dict[str, MutableSet[str]] = {}
        for sentence in treebank.sentences:
            for row in sentence.rows:
                if row.lemma in forms:
                    forms[row.lemma].add(row.token)
                else:
                    forms[row.lemma] = set([row.token])

        form_counts = []
        for lemma in forms:
            form_counts.append(len(forms[lemma]))

        if sum(form_counts) == 0:
            print("Warning: WordFormsPerLemma is 0 for treebank " +
                  treebank.lang_code)

        try:
            return sum(form_counts) / len(form_counts)
        except ZeroDivisionError:
            return 0
