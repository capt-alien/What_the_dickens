# generates histogram from textfile

from sys import argv
import re
import random
import tokenize
import cleanup


## Create a dictionary with counts
def dict_words(words):
    #takes a list argument and returns a word count
    dict = {}
    for word in words:
        if word not in (dict):
            dict[word] = 0
        dict[word] += 1
    return dict

## create a list of lists with counts takes in the words in unique words list
def list_words(words):
    #takes a list argument and returns a word count
    words_list = []
    unique_words = tokenize.unique_list(words)
    for word in unique_words:
        #adds unique value to words list
            words_list.append([word, words.count(word)])
    return words_list

##Create a list of tuples
def tuple(words):
    #takes a list argument and returns a word count
    tuple_list = []
    for word in words:
        if (word, words.count(word)) not in tuple_list:
            tuple_list.append((word, words.count(word)))
    return tuple_list

#sums dictionary in histo
def sum_value(histogram):
    total = (sum(histogram.values()))
    return total

#opens file_name
if __name__ == '__main__':
    file1 = argv[1]
    print_list = cleanup.text_list(file1)
    #promts user for method
    print("==================================")
    print("Welcome to Hist-o-grama-rama!!!!!")
    print("=======>INSTRUCTIONS<============")
    print("Press 1 for a Dictionary")
    print("Press 2 for a List of Lists")
    print("Press 3 for a Tuple")
    input1 = input("Which method would you like returned? ")
    #dictionary
    if input1 == "1":
        dict_list = dict_words(print_list)
        tots = sum_value(dict_list)
        print(dict_list)
        print(tots)

    #list of list
    elif input1 == "2":
        wlist = list_words(print_list)
        print(wlist)

    #Tuple
    elif input1 == "3":
        tlist = tuple(print_list)
        print(tlist)

#else statement
    else:
        print("Incorect input, Please try again!")
