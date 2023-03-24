from dataclasses import dataclass
from typing import List
from .Sentence import Sentence
from ..parsers.ConnluParser import ConnluParser
import random


@dataclass
class Treebank:
    sentences: List[Sentence]
    lang_code: str

    def __str__(self) -> str:
        return f"Treebank(lang_code={self.lang_code}, sentences=[{len(self.sentences)} sentences)])"

    @classmethod
    def from_file(cls, path, lang_code=None, ignore_compound_indexes=False):
        sentences = ConnluParser.parse(
            path, lang_code, ignore_compound_indexes=ignore_compound_indexes)
        return cls(sentences=sentences, lang_code=lang_code)

    @classmethod
    def split(cls, treebank=None, split_size: float = 0.5):
        sentences: List[Sentence] = [*treebank.sentences]
        random.shuffle(sentences)
        split_1_num_sents = int(len(sentences) * split_size)
        sents_1 = sentences[:split_1_num_sents]
        sents_2 = sentences[split_1_num_sents:]

        tb_1 = cls(sentences=sents_1, lang_code=treebank.lang_code)
        tb_2 = cls(sentences=sents_2, lang_code=treebank.lang_code)

        return tb_1, tb_2

    @classmethod
    def merge(cls, tb_1, tb_2):
        return cls(sentences=tb_1.sentences + tb_2.sentences, lang_code=tb_1.lang_code)
