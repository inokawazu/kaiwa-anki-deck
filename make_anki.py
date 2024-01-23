import pandas as pd
import sys
import os

# initial fields: id,japanese,english,particle,word,kanji,furigana,obi2


def obi_str_to_num(sobi: str) -> int:
    return int(sobi.split()[0])


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <inputfile.csv>")
        quit()
    sents = pd.read_csv(sys.argv[1])
    col = sents["obi2"]
    sents["obi2_int"] = col.map(obi_str_to_num)
    sents.sort_values("obi2_int", inplace=True)
    sents['anki_tags'] = 'id::' + sents['id'].astype(str)\
        + ' particle::' + sents['particle']\
        + ' word::' + sents['word']\
        + ' kanji::' + sents['kanji'].map(lambda s: s.replace(",", "-"))\
        + ' obi::' + sents['obi2_int'].astype(str)
    sents['anki_tags'] = sents['anki_tags']
    sents.to_csv("anki_kaiwa.csv", index=False, header=False)


if __name__ == "__main__":
    main()
