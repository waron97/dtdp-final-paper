from .Metric import Metric
from ..boxes.Sentence import Sentence


class VerbsExplicitSubject(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        verbs = [row for row in sentence.rows if row.pos == "VERB"]
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
