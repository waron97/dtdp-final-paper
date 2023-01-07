from .Metric import Metric


class TokenCount(Metric):
    include_punct = False

    def __init__(self, include_punct=False) -> None:
        super().__init__()
        self.include_punct = include_punct

    def for_sentence(self, sentence):
        if self.include_punct:
            return len(sentence.rows)
        filtered = [row for row in sentence.rows if row.pos != 'PUNCT']
        return len(filtered)
