from src.boxes.Treebank import Treebank
from src.metrics.TokenCount import TokenCount
from src.metrics.TreeDepth import TreeDepth
from src.metrics.LengthLongestDepLink import LengthLongestDepLink
from src.metrics.NounVerbRatio import NounVerbRatio
from src.metrics.ClausesPerSentence import ClausesPerSentence
from src.metrics.XcompCcompCount import XCOMP_Count, CCOMP_Count
from src.metrics.VerbsExplicitSubject import VerbsExplicitSubject
from src.metrics.TypeTokenRatio import TypeTokenRatio
from src.metrics.WordFormsPerLemma import WordFormsPerLemma
from src.metrics.TriPosVariety import TriPosVariety
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
        ("en_atis", en_atis),
        ("en_ewt", en_ewt),
        ("en_gum", en_gum),
        ("de_gsd", de_gsd),
        ("de_hdt", de_hdt),
        ("hun_szeged_1", hun_szeged_1),
        ("hun_szeged_2", hun_szeged_2),
        ("cmn_gsd", cmn_gsd),
        ("cmn_pud", cmn_pud),
    ]

    # for name, bank in treebanks:
    #     print(name, len(bank.sentences))

    sentence_level_metrics = [
        ("tc", TokenCount(include_punct=False)),
        ("ttr", TypeTokenRatio()),
        ("ptd", TreeDepth()),
        ("lldl", LengthLongestDepLink()),
        ("n2v", NounVerbRatio()),
        ("cxc", ClausesPerSentence()),
        ("xcomp", XCOMP_Count()),
        ("ccomp", CCOMP_Count()),
        ("vesr", VerbsExplicitSubject()),
    ]

    treebank_level_metrics = [
        ("wfpl", WordFormsPerLemma()),
        ("vsp", TriPosVariety())
    ]

    df = pd.DataFrame(index=[i[0] for i in treebanks],
                      columns=[i[0] for i in sentence_level_metrics] + [i[0] for i in treebank_level_metrics])

    for treebank_name, treebank in treebanks:
        for metric_name, metric in sentence_level_metrics:
            result = metric.for_treebank(
                treebank).mean()
            df.loc[treebank_name, metric_name] = round(result, 4)
        for metric_name, metric in treebank_level_metrics:
            result = metric.compute(treebank)
            df.loc[treebank_name, metric_name] = round(result, 4)

    print(df)

    # ---------------------

    out_table = ["\\begin{table*}", "\\centering"]

    metric_names = [i[0] for i in sentence_level_metrics] + [i[0]
                                                             for i in treebank_level_metrics]

    l = int(len(metric_names) / 2)

    n1 = metric_names[:l]
    n2 = metric_names[l:]
    s1 = " & ".join([f"\\textbf{{{i}}}" for i in n1])
    s2 = " & ".join([f"\\textbf{{{i}}}" for i in n2])

    # ---------------------
    # Tabular 1
    # ---------------------

    out_table.append(
        f"\\begin{{tabularx}}{{\\textwidth}}{{X{'c' * len(n1)}}}")
    out_table.append("\\hline")
    out_table.append(f"\\textbf{{Treebank}} & {s1} \\\\")
    out_table.append("\\hline")
    for name, treebank in treebanks:
        metric_values = " & ".join([str(df.loc[name, i]) for i in n1])
        out_table.append(f"{name} & {metric_values} \\\\")
        out_table.append("\\hline")
    out_table.append("\\end{tabularx}")

    # ---------------------
    # Tabular 2
    # ---------------------

    out_table.append("")
    out_table.append("\\vspace{0.5cm}")
    out_table.append("")

    # ---------------------

    out_table.append(
        f"\\begin{{tabularx}}{{\\textwidth}}{{X{'c' * len(n2)}}}")
    out_table.append("\\hline")
    out_table.append(f"\\textbf{{Treebank}} & {s2} \\\\")
    out_table.append("\\hline")
    for name, treebank in treebanks:
        metric_values = " & ".join([str(df.loc[name, i]) for i in n2])
        out_table.append(f"{name} & {metric_values} \\\\")
        out_table.append("\\hline")
    out_table.append("\\end{tabularx}")

    # ---------------------

    out_table.append("\\caption{{Results}}")
    out_table.append("\\label{{tab:results}}")
    out_table.append("\\end{table*}")

    with open("paper/tables/results.tex", "w", encoding="utf-8") as f:
        lines = "\n".join([l.replace("_", "\\_") for l in out_table])
        f.write(lines)


if __name__ == '__main__':
    main()
