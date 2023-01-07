from .Row import Row
from typing import List
import numpy as np


class ParseTree:
    adjacency: np.ndarray
    rows: List[Row]
    root_index: int

    def __init__(self, rows: List[Row], root_index: int) -> None:
        self.rows = rows
        self.root_index = root_index
        self.__bootstrap_adjacency_matrix()

    def __bootstrap_adjacency_matrix(self):
        l = len(self.rows)
        dimensions = (l, l)
        arr = np.full(dimensions, False)
        for i, row in enumerate(self.rows):
            for j, r in enumerate(self.rows):
                if r.head_index == row.index:
                    arr[i, j] = True
        self.adjacency = arr

    def depth(self):
        pass
