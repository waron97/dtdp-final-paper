from .Metric import TreebankLevelMetric
from ..boxes.Treebank import Treebank
from typing import List


class VerbsExplicitSubject(TreebankLevelMetric):
    def __init__(self, verb_pos: List[str] = ["VERB"]) -> None:
        super().__init__()
        self.verb_pos = verb_pos

    def compute(self, treebank: Treebank) -> float:
        n_verbs = 0
        n_with_explicit_subject = 0
        for sentence in treebank.sentences:
            verbs = [row for row in sentence.rows if row.pos in self.verb_pos]
            for verb_row in verbs:
                n_verbs += 1
                connecting = [
                    row.rel_type for row in sentence.rows if row.head_index == verb_row.index]
                if "nsubj" in connecting or "csubj" in connecting:
                    n_with_explicit_subject += 1
        return n_with_explicit_subject / n_verbs
