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
    for character in text:
        if character not in punctuation:
            no_punctuation = no_punctuation + character
    
    text_lower = no_punctuation.lower()
    
    split_text = text_lower.split()
    
    new_text = [n_text for n_text in split_text if not n_text in STOP_WORDS]
    
    repeated_text = dict()
    for word in new_text:
        if word in repeated_text:
            repeated_text[word] += 1
        else:
            repeated_text[word] = 1
    
    repeated_text = {key: value for key, value in repeated_text.items() if value >=6}
    
    sorted_text = sorted(repeated_text.items(), key=lambda seq: seq[0], reverse=False)
    
    for key, value in sorted_text:
        print (key.rjust(15) , ' | ', value, value * ('*'))

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
