import random
from sys import argv
import cleanup
import tokenize
import wordcount


# create a sum of key values in dict
#sums dictionary in histo
def sum_value(hist):
    dict_total = int((sum(hist.values())))
    return dict_total

# takes a histogram and returns a weighted probabibility
def weighted_random(hist, total):
    destination = random.randint(0, total)
    for word in hist:
        destination = destination - hist[word]
        if destination <= 0:
            return word

if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    #processing words and defineing objects
    words = cleanup.text_list(file1)
    hist1 = wordcount.dict_words(words)
    total = sum_value(hist1)
    print(total)
    print(weighted_random(hist1, total))
    # print(analysis1)
