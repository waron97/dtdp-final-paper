from typing import List
from ..boxes.Row import Row
from .core import find_index
from ..boxes.ParseTree import ParseTree


def get_depth(rows: List[Row], root_index: int = None) -> int:
    """Compute distance from root to deepest leaf node."""
    if root_index is None:
        # If root_index is not provided, find it:
        # - If a row has head_index 0, it is the root
        # - If a row has its head outside of the context of the provided tree, it is the root

        indexes = [r.index for r in rows]

        def head_not_in_rows(row: Row):
            return row.head_index not in indexes

        root_index = find_index(
            lambda row: row.head_index == 0 or head_not_in_rows(row), rows)

    if not rows or len(rows) == 0:
        return 0
    return ParseTree(rows, root_index).depth()
