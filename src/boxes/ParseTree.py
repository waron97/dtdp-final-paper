from .Row import Row
from typing import List, Callable
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

    def depth(self) -> int:
        max_depth = 0

        def on_visit(row: Row, index: int, depth: int):
            nonlocal max_depth
            if depth > max_depth:
                max_depth = depth

        self.__traverse(on_visit=on_visit)
        return max_depth

    def __traverse(self, depth: int = 0, start_index: int = None, on_visit: Callable[[Row, int, int], None] = None):
        if start_index is None:
            start_index = self.root_index

        if on_visit is not None:
            on_visit(self.rows[start_index], start_index, depth)

        children = self.__get_children_indexes(start_index)

        for child_index in children:
            self.__traverse(depth=depth + 1,
                            start_index=child_index, on_visit=on_visit)

    def __get_children_indexes(self, index: int) -> List[int]:
        children_indexes = []
        for i in range(len(self.adjacency[index])):
            if self.adjacency[index][i]:
                children_indexes.append(i)
        return children_indexes
