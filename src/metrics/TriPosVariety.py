from .Metric import TreebankLevelMetric
from ..boxes.Treebank import Treebank
from typing import MutableSet, Tuple


class TriPosVariety(TreebankLevelMetric):
    def compute(self, treebank: Treebank) -> float:
        tri_pos: MutableSet[Tuple[str, str, str]] = set()
        for sentence in treebank.sentences:
            for i in range(0, len(sentence.rows) - 2):
                a, b, c = sentence.rows[i], sentence.rows[i +
                                                          1], sentence.rows[i + 2]
                tri_pos.add((a.pos, b.pos, c.pos))
        return len(tri_pos)
