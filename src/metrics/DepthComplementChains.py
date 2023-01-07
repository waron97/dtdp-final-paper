from .Metric import Metric
from ..boxes.Sentence import Sentence


class DepthComplementChains(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        return super().for_sentence(sentence)
