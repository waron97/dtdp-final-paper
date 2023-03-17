from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
from src.metrics.LengthLongestDepLink import LengthLongestDepLink
from src.util import download_experiment_treebanks
from src.constants.treebank_paths import WEB_TREEBANK_PATHS
import pandas as pd


def main():
    download_experiment_treebanks()

    de_gsd = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_gsd'], lang_code='de_gsd', ignore_compound_indexes=True)

    en_asl = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_esl'], lang_code='en_esl', ignore_compound_indexes=True)

    en_atis = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_atis'], lang_code='en_atis', ignore_compound_indexes=True)

    de_hdt_1 = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_hdt_1'], lang_code='de_hdt_1', ignore_compound_indexes=True)

    de_hdt_2 = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_hdt_2'], lang_code='de_hdt_2', ignore_compound_indexes=True)

    en_gum = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_gum'], lang_code='en_gum', ignore_compound_indexes=True)

    en_ewt = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_ewt'], lang_code='en_ewt', ignore_compound_indexes=True)

    treebanks = [
        ("en_esl", en_asl),
        ("en_ewt", en_ewt),
        ("en_gum", en_gum),
        ("en_atis", en_atis),
        ("de_gsd", de_gsd),
        ("de_hdt_1", de_hdt_1),
        ("de_hdt_2", de_hdt_2),
    ]

    metrics = [
        ("token count", TokenCount(include_punct=False)),
        ("tree depth", TreeDepth()),
        ("lldl", LengthLongestDepLink())
    ]

    df = pd.DataFrame(index=[i[0] for i in treebanks],
                      columns=[i[0] for i in metrics])

    for treebank_name, treebank in treebanks:
        for metric_name, metric in metrics:
            df.loc[treebank_name, metric_name] = metric.for_treebank(
                treebank).mean()

    print(df)


if __name__ == '__main__':
    main()
