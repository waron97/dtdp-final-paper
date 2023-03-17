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
    try:
        os.makedirs(data_dir)
    except:
        pass

    urls = [
        ("en_atis.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-Atis/master/en_atis-ud-train.conllu"),
        ("en_esl.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_English-ESL/master/en_esl-ud-train.conllu"),
        ("de_gsd.conllu", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-train.conllu"),
        ("de_hdt_1", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/master/de_hdt-ud-train-a-1.conllu"),
        ("de_hdt_2", "https://raw.githubusercontent.com/UniversalDependencies/UD_German-HDT/master/de_hdt-ud-train-a-2.conllu"),
    ]

    for filename, url in urls:
        p = os.path.join(data_dir, filename)
        download_treebank(p, url)
