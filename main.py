from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
from src.metrics.LengthLongestDepLink import LengthLongestDepLink
from src.util import download_experiment_treebanks
from src.constants.treebank_paths import WEB_TREEBANK_PATHS


def main():
    download_experiment_treebanks()

    de_gsd = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_gsd'], lang_code='de_gsd', ignore_compound_indexes=True)

    en_asl = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_esl'], lang_code='en_esl', ignore_compound_indexes=True)

    # Length of longest dependency link
    lengthLongestDepLink = LengthLongestDepLink()
    result_de = lengthLongestDepLink.for_treebank(de_gsd)
    result_en = lengthLongestDepLink.for_treebank(en_asl)

    print("[de length of longest dependency link]", result_de.mean())
    print("[en length of longest dependency link]", result_en.mean())

    # token count
    tokenCount = TokenCount(include_punct=False)
    result_de = tokenCount.for_treebank(de_gsd)
    result_en = tokenCount.for_treebank(en_asl)

    print("[de token count]", result_de.mean())
    print("[en token count]", result_en.mean())

    # parse tree depth
    treeDepth = TreeDepth()
    result_de = treeDepth.for_treebank(de_gsd)
    result_en = treeDepth.for_treebank(en_asl)
    print("[de tree depth]", result_de.mean())
    print("[en tree depth]", result_en.mean())


if __name__ == '__main__':
    main()
