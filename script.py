from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
import os


def main():
    eng_path = os.path.join(os.path.dirname(__file__), 'corpus/en.conllu')
    eng = Treebank.from_file(eng_path, 'en')
    deu_path = os.path.join(os.path.dirname(__file__), 'corpus/deu.conllu')
    deu = Treebank.from_file(deu_path, 'deu')
    hun_path = os.path.join(os.path.dirname(__file__), 'corpus/hun.conllu')
    hun = Treebank.from_file(hun_path, 'hun')
    mandarin_path = os.path.join(
        os.path.dirname(__file__), 'corpus/madarin.conllu')
    mandarin = Treebank.from_file(mandarin_path, 'cmn')

    tokenCount = TokenCount(include_punct=False)
    tokenCountResult = tokenCount.for_parellel_treebanks(
        [deu, hun, mandarin], reference_treebank=eng)


if __name__ == '__main__':
    main()
