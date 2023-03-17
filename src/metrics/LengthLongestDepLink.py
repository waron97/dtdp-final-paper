from .Metric import Metric
from ..boxes.Sentence import Sentence


class LengthLongestDepLink(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        longest_so_far = 0
        for word in sentence.rows:
            head = word.head_index
            index = word.index
            distance = abs(int(head) - int(index))
            if distance > longest_so_far:
                longest_so_far = distance
        return longest_so_far
