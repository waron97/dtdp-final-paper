from src.metrics.Metric import Metric
from ..boxes.Sentence import Sentence


class XCOMP_Count(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        xcomp_rel_types = ["xcomp"]
        return len([row for row in sentence.rows if row.rel_type in xcomp_rel_types])


class CCOMP_Count(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        xcomp_rel_types = ["ccomp"]
        return len([row for row in sentence.rows if row.rel_type in xcomp_rel_types])
