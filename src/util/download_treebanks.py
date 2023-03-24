import requests
import os


def download_treebank(filename, url):
    if os.path.exists(filename):
        return

    response = requests.get(url)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)


def download_experiment_treebanks():
    data_dir = os.path.join(os.getcwd(), "assets", "web_treebanks")
    course_data_dir = os.path.join(os.getcwd(), "assets", "course_treebanks")

    try:
        os.makedirs(data_dir)
    except:
        pass
    try:
        os.makedirs(course_data_dir)
    except:
        pass

    urls = [
        ("en_atis.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-Atis/master/en_atis-ud-train.conllu"),
        ("en_esl.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-ESL/master/en_esl-ud-train.conllu"),
        ("de_gsd.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-train.conllu"),
        ("de_hdt_1.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/master/de_hdt-ud-train-a-1.conllu"),
        ("de_hdt_2.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/master/de_hdt-ud-train-a-2.conllu"),
        ("en_gum.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-GUM/master/en_gum-ud-train.conllu"),
        ("en_ewt.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-train.conllu"),
        ("hun_szeged.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_Hungarian-Szeged/master/hu_szeged-ud-train.conllu"),
        ("cmn_gsd.conllu", "https://github.com/UniversalDependencies/UD_Chinese-GSD/raw/master/zh_gsd-ud-train.conllu"),
        ("cmn_pud.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_Chinese-PUD/master/zh_pud-ud-test.conllu")
    ]

    course_urls = [
        ("deu.conllu", "https://raw.githubusercontent.com/iscl-dtdp/ParallelTreebank-FinalProject/main/deu.conllu?token=GHSAT0AAAAAAB5G54BWXQXH44Y54D2BZ3BUZA5WY7A"),
        ("en.conllu", "https://raw.githubusercontent.com/iscl-dtdp/ParallelTreebank-FinalProject/main/en.conllu?token=GHSAT0AAAAAAB5G54BWF6Y6VYJHHWIMLG3KZA5WZ5A"),
        ("hun.conllu", "https://raw.githubusercontent.com/iscl-dtdp/ParallelTreebank-FinalProject/main/hun.conllu?token=GHSAT0AAAAAAB5G54BX3NZS3XGE6LTUF5IEZA5W2CQ"),
        ("mandarin.conllu", "https://raw.githubusercontent.com/iscl-dtdp/ParallelTreebank-FinalProject/main/madarin.conllu?token=GHSAT0AAAAAAB5G54BXMWYAHGANEJP42G2KZA5W2IQ"),
    ]

    for filename, url in urls:
        p = os.path.join(data_dir, filename)
        download_treebank(p, url)

    for filename, url in course_urls:
        p = os.path.join(course_data_dir, filename)
        download_treebank(p, url)
