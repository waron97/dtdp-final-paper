from .Metric import Metric
from ..boxes.Sentence import Sentence


class NounVerbRatio(Metric):
    def for_sentence(self, sentence: Sentence) -> float:
        noun_pos_tags = ["NOUN", "PROPN"]
        verb_pos_tags = ["VERB", "AUX"]
        count_nouns = len(
            [row for row in sentence.rows if row.pos in noun_pos_tags])
        count_verbs = len(
            [row for row in sentence.rows if row.pos in verb_pos_tags])
        try:
            return count_nouns / count_verbs
        except ZeroDivisionError:
            return 0
