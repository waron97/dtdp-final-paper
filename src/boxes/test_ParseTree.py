from .ParseTree import ParseTree
from .Row import Row
import numpy as np


def test_parse_1():
    rows = [
        Row(index=1, head_index=0, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=2, head_index=1, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=3, head_index=1, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=4, head_index=2, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=5, head_index=2, token="",
            lemma="", pos="", rel_type="", attrs={}),
    ]

    tree = ParseTree(rows, root_index=0)

    exp = np.array([
        [False, True, True, False, False],
        [False, False, False, True, True],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
    ])

    assert np.array_equal(tree.adjacency, exp)


def test_parse_1():
    rows = [
        Row(index=1, head_index=0, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=2, head_index=1, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=3, head_index=1, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=4, head_index=2, token="",
            lemma="", pos="", rel_type="", attrs={}),
        Row(index=5, head_index=2, token="",
            lemma="", pos="", rel_type="", attrs={}),
    ]

    tree = ParseTree(rows, root_index=0)

    assert tree.depth() == 2
