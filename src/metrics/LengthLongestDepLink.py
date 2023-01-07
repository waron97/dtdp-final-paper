from .Metric import Metric
from ..boxes.Sentence import Sentence


class LengthLongestDepLink(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        return super().for_sentence(sentence)
