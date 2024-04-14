import argparse
import pickle as pkl
from transliterate.MyTransliterator import Transliterator


def convert_to_ascii(string):
    dict_ = {
        u"ṅ": "GN",
        u"ñ": "JN",
        u"ṭ": "T",
        u"ṭh": "Th",
        u"ḍ": "D",
        u"ḍh": "Dh",
        u"ṇ": "N",
        u"ś": "S",
        u"ṣ": "sh",
        u"ḷ": "L",
        u"ṟ": "R",
        u"ṛ": "rh",
        u"ṝ": "Rh",
        u"ḻa": "zh",
        u"l̥̄": "LH",
        u"ā": "A",
        u"ī": "I",
        u"ū": "U",
        u"ē": "E",
        u"ō": "O",
        u"m̐": "Nh",
        u"ṁ": "M",
        u"ḥ": "H",
        u"ṉa": "NH",
    }
    replaced_string = string
    for key, value in dict_.items():
        replaced_string = replaced_string.replace(key, value)
    return replaced_string


def transliterate(all_data, lang):
    """
    "all_data": a list of lists.
                Each list has text to be transliterated.
    "lang": "Telugu", "Kannada", "Tamil", "Malayalam", "Hindi"

    returns transliterated lists
    """
    transliterator = Transliterator(lang)

    transliterated = []
    if isinstance(all_data, list):
        for each_data in all_data:
            transliterated.append(
                convert_to_ascii(transliterator.transliterate(each_data)))
    if isinstance(all_data, str):
        transliterated = convert_to_ascii(
            transliterator.transliterate(all_data))

    return transliterated


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transliterate given text.')
    parser.add_argument('--data_file', type=str,
                        help='File containing all data')
    parser.add_argument('--lang', type=str,
                        help='Language to Transliterate')
    parser.add_argument('--out_file', type=str, default="data_transliterated.txt", required=False,
                        help='Output file')

    args = parser.parse_args()

    # Load all_data from a file
    if args.data_file.endswith(".pkl"):
        all_data = pkl.load(open(args.data_file, "rb"))
    else:
        # Load all_data from a text file
        with open(args.data_file, 'r', encoding="utf-8") as file:
            all_data = [line for line in file]

    transliterated = transliterate(all_data, args.lang)

    # Save all_tokens to a text file
    with open(args.out_file, 'w') as file:
        for each_line in transliterated:
            file.write(each_line)
