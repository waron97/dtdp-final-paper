from dataclasses import dataclass
from typing import List
from .Row import Row
import pandas as pd


@dataclass
class Sentence:
    rows: List[Row]
    sent_id: int
    sent_id_eng: int
    lang_code: str
    text: str
    text_eng: str

    def to_pandas(self):
        return pd.DataFrame([row.to_dict() for row in self.rows])
