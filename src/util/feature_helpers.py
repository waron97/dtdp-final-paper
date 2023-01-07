from typing import List
from ..boxes.Row import Row
from .core import find_index


def get_depth(rows: List[Row], root_index=None) -> int:
    """Compute distance from root to deepest leaf node."""
    if root_index is None:
        # If root_index is not provided, find it:
        # - If a row has head_index 0, it is the root
        # - If a row has its head outside of the context of the provided tree, it is the root
        def head_not_in_rows(row): return row.head_index not in [
            r.index for r in rows]
        root_index = find_index(
            lambda row: row.head_index == 0 or head_not_in_rows(row))
    return 0
