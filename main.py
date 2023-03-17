from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
from src.util import download_experiment_treebanks
from src.constants.treebank_paths import WEB_TREEBANK_PATHS


def main():
    download_experiment_treebanks()

    de_gsd = Treebank.from_file(WEB_TREEBANK_PATHS['de_gsd'])

    # token count
    tokenCount = TokenCount(include_punct=False)

    # parse tree depth
    treeDepth = TreeDepth()


if __name__ == '__main__':
    main()
