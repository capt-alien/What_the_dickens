from sys import argv
import re
import random


##open text file and turn it into a usable words_list
def text_list(file_name):
    raw_words = open(file_name, 'r').read().lower()
    tokens = re.sub(r"\." , " STOP START ", raw_words)
    wo_punctuation = re.sub(r"\W", " " , tokens)
    word_pasta = wo_punctuation.split()
    if word_pasta[(len(word_pasta)-1)] == 'START':
        word_pasta.pop()
    if word_pasta[0] != 'START':
        word_pasta.insert(0,'START')
    return word_pasta


if __name__ == '__main__':
    file1 = argv[1]
    print(text_list(file1))
