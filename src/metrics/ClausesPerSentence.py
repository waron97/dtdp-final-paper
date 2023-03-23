from .Metric import Metric
from ..boxes.Sentence import Sentence


class ClausesPerSentence(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        sent_sep_rel_types = ["xcomp", "ccomp", "advcl",
                              "acl", "acl:relcl", "csubj", "csubj:pass", "cc"]
        return len([row for row in sentence.rows if row.rel_type in sent_sep_rel_types])
