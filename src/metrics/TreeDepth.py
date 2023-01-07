from .Metric import Metric
from ..boxes.Sentence import Sentence
from ..util.feature_helpers import get_depth


class TreeDepth(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        return get_depth(sentence.rows)
