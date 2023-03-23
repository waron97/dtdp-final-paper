from .Metric import Metric
from ..boxes.Sentence import Sentence


class TypeTokenRatio(Metric):

    def for_sentence(self, sentence: Sentence) -> float:
        tokens = [row.token for row in sentence.rows]
        lemmas = set([row.token for row in sentence.rows])
        return len(lemmas) / len(tokens)
