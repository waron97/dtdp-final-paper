import pandas as pd
from typing import List, Tuple
from pprint import pprint


def _get_split_lines(
    df: pd.DataFrame,
    row_labels: List[str] = [],
    col_labels: List[str] = [],
    main_row_label: str = "Treebank",
    highlights: List[Tuple[str, str]] = [],

):
    col_def = f"X{'c' * len(col_labels)}"
    lines = [f"\\begin{{tabularx}}{{\\textwidth}}{{{col_def}}}", "\\hline"]
    headers = [f"\\textbf{{{main_row_label}}}"] + \
        [f"\\textbf{{{i}}}" for i in col_labels]
    headers = " & ".join(headers) + " \\\\"
    lines.append(headers)
    lines.append("\\hline")

    for label in row_labels:
        line = [label]
        for column in col_labels:
            part = f"{df.loc[label, column]}"
            coords = (label, column)
            if coords in highlights:
                part = f"\\textbf{{{part}}}"
            line.append(part)
        lines.append(" & ".join(line) + " \\\\")
        lines.append("\\hline")

    lines.append("\\end{tabularx}")
    return lines


def write_to_latex(
    df: pd.DataFrame,
    outfile: str,
    n_splits: int = 1,
    transpose: bool = False,
    caption: str = "",
    ref: str = ""
):
    main_row_label = "Treebank"

    if transpose:
        df = df.transpose()
        main_row_label = "Metric"

    row_labels = list(df.index)
    col_labels = list(df.columns)

    highlights = []
    # print(df)
    for col in col_labels:
        series: pd.Series = df[col]
        sort = series.argsort()
        highest = sort[-1]
        second_highest = sort[-2]
        third_highest = sort[-3]
        highlights.append((row_labels[highest], col))
        highlights.append((row_labels[second_highest], col))
        highlights.append((row_labels[third_highest], col))

    lines = ["\\begin{table*}", "\\centering"]

    split_labels: List[Tuple[List[str], List[str]]] = []
    indexes_per_split = int(len(col_labels) / n_splits)

    if n_splits == 1:
        split_labels = [
            (row_labels, col_labels)
        ]
    elif n_splits == 2:
        split_labels = [
            (row_labels, col_labels[:indexes_per_split]),
            (row_labels, col_labels[indexes_per_split:])
        ]

    for i, (rows, cols) in enumerate(split_labels):
        split_lines = _get_split_lines(
            df,
            row_labels=rows,
            col_labels=cols,
            main_row_label=main_row_label,
            highlights=highlights
        )
        lines.extend(split_lines)
        if i != len(split_labels) - 1:
            lines.extend(["", "\\vspace{0.5cm}", ""])

    lines.append(
        f"\\caption{{{caption}}}")
    lines.append(f"\\label{{{ref}}}")
    lines.append("\\end{table*}")

    lines = "\n".join(lines).replace("_", "\\_")
    with open(outfile, "w") as f:
        f.write(lines)
