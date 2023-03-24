from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
from src.metrics.LengthLongestDepLink import LengthLongestDepLink
from src.metrics.NounVerbRatio import NounVerbRatio
from src.metrics.ClausesPerSentence import ClausesPerSentence
from src.metrics.XcompCcompCount import XCOMP_Count, CCOMP_Count
from src.metrics.VerbsExplicitSubject import VerbsExplicitSubject
from src.metrics.TypeTokenRatio import TypeTokenRatio
from src.util import download_experiment_treebanks
from src.constants.treebank_paths import WEB_TREEBANK_PATHS
import pandas as pd


def main():
    download_experiment_treebanks()

    de_gsd = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_gsd'], lang_code='de_gsd', ignore_compound_indexes=True)

    en_asl = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_esl'], lang_code='en_esl', ignore_compound_indexes=True)

    de_hdt_1 = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_hdt_1'], lang_code='de_hdt_1', ignore_compound_indexes=True)

    de_hdt_2 = Treebank.from_file(
        WEB_TREEBANK_PATHS['de_hdt_2'], lang_code='de_hdt_2', ignore_compound_indexes=True)

    de_hdt = Treebank.merge(de_hdt_1, de_hdt_2)

    en_gum = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_gum'], lang_code='en_gum', ignore_compound_indexes=True)

    en_ewt = Treebank.from_file(
        WEB_TREEBANK_PATHS['en_ewt'], lang_code='en_ewt', ignore_compound_indexes=True)

    hun_szeged = Treebank.from_file(
        WEB_TREEBANK_PATHS["hun_szeged"], lang_code="hun_szeged", ignore_compound_indexes=True)
    hun_szeged_1, hun_szeged_2 = Treebank.split(hun_szeged, 0.5)

    cmn_gsd = Treebank.from_file(
        WEB_TREEBANK_PATHS["cmn_gsd"], lang_code="cmn_gsd", ignore_compound_indexes=True)

    cmn_pud = Treebank.from_file(
        WEB_TREEBANK_PATHS["cmn_pud"], lang_code="cmn_pud", ignore_compound_indexes=True)

    treebanks = [
        ("en_esl", en_asl),
        ("en_ewt", en_ewt),
        ("en_gum", en_gum),
        ("de_gsd", de_gsd),
        ("de_hdt", de_hdt),
        ("hun_szeged_1", hun_szeged_1),
        ("hun_szeged_2", hun_szeged_2),
        ("cmn_gsd", cmn_gsd),
        ("cmn_pud", cmn_pud)
    ]

    for name, bank in treebanks:
        print(name, len(bank.sentences))

    metrics = [
        ("token count", TokenCount(include_punct=False)),
        ("type token ratio", TypeTokenRatio()),
        ("tree depth", TreeDepth()),
        ("lldl", LengthLongestDepLink()),
        ("nv-ratio", NounVerbRatio()),
        ("CxC", ClausesPerSentence()),
        ("xcomp_c", XCOMP_Count()),
        ("ccomp_c", CCOMP_Count()),
        ("vesr", VerbsExplicitSubject())

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
