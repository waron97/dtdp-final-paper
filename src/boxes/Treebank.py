from dataclasses import dataclass
from typing import List
from .Sentence import Sentence
from ..parsers.ConnluParser import ConnluParser


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
