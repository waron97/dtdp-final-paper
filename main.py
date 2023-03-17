from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
import os


def main():

    # token count
    tokenCount = TokenCount(include_punct=False)

    # parse tree depth
    treeDepth = TreeDepth()


if __name__ == '__main__':
    main()
