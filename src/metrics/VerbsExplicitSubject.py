from .Metric import Metric
from ..boxes.Sentence import Sentence
from typing import List


class VerbsExplicitSubject(Metric):
    def __init__(self, verb_pos: List[str] = ["VERB"]) -> None:
        super().__init__()
        self.verb_pos = verb_pos

    def for_sentence(self, sentence: Sentence) -> float:
        verbs = [row for row in sentence.rows if row.pos in self.verb_pos]
        with_explicity_subject = 0
        for verb_row in verbs:
            connecting = [
                row.rel_type for row in sentence.rows if row.head_index == verb_row.index]
            if "nsubj" in connecting or "csubj" in connecting:
                with_explicity_subject += 1
        try:
            return (with_explicity_subject / len(verbs))
        except ZeroDivisionError:
            return 0
