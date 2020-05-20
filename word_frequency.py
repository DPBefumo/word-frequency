STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string
punctuation = string.punctuation

def print_word_freq(file):
    opened_file = open(file)
    text = opened_file.read()
    no_punctuation = ""
    for punc in text:
        if punc not in punctuation:
            no_punctuation = no_punctuation + punc
    text_lower = no_punctuation.lower()
    split_text = text_lower.split(" ")
    new_text = []
    for n_text in split_text:
        if not n_text in STOP_WORDS:
            new_text.append(n_text)
    print(new_text)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
