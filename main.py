from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
import os


def main():
    eng_path = os.path.join(os.path.dirname(__file__), 'corpus/en.conllu')
    eng = Treebank.from_file(eng_path, 'eng', ignore_compound_indexes=True)
    deu_path = os.path.join(os.path.dirname(__file__), 'corpus/deu.conllu')
    deu = Treebank.from_file(deu_path, 'deu', ignore_compound_indexes=True)
    hun_path = os.path.join(os.path.dirname(__file__), 'corpus/hun.conllu')
    hun = Treebank.from_file(hun_path, 'hun', ignore_compound_indexes=True)
    mandarin_path = os.path.join(
        os.path.dirname(__file__), 'corpus/madarin.conllu')
    mandarin = Treebank.from_file(
        mandarin_path, 'cmn', ignore_compound_indexes=True)

    # token count
    tokenCount = TokenCount(include_punct=False)
    tokenCountResult = tokenCount.for_parellel_treebanks(
        [deu, hun, mandarin], reference_treebank=eng)
    # print(tokenCountResult.to_pandas())

    # parse tree depth
    treeDepth = TreeDepth()
    treeDepthResult = treeDepth.for_parellel_treebanks(
        [deu, hun, mandarin, eng])
    print(treeDepthResult.to_pandas())
    print(treeDepthResult)


if __name__ == '__main__':
    main()
