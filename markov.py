# Drew on code from the following artical borrowed code from Faith C.:
# https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
from sys import argv
import cleanup
import sample
import sentence
import dictogram
import random

#please note that I reverse engineered this from the nth order chain
def m_chain_one(text_list):
    markov_dict = {}
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - 1):
        window = text_list[index]
        if index in markov_dict:
            markov_dict[window].add_count([text_list[index + 1]])
        else:
            markov_dict[window] = dictogram.Dictogram([text_list[index + 1]])
    # return dictionary
    return markov_dict

#nth Order markov Chain derived from first order
def order_mchain(order, text_list):
    markov_dict = {}
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - order):
        # text_list[index] should be our word from list
        window = tuple(text_list[index: index + order])
        # check if window is stored in the dictionary already
        if window in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[window].add_count([text_list[index + order]])
        else:
            # if not, create new entry with window as key and dictogram as value
            markov_dict[window] = dictogram.Dictogram([text_list[index + order]])
    # return dictionary
    return markov_dict

def start_token(markov_model):
    # generate a random word followin START in a corpus
    start_tokens= []
    for key in markov_model:
        if key[0] == "START":
            start_tokens.append(key)
    token = random.choice(start_tokens)
    return token

#unessary for this ittration but keeping for future improvments
def stop_tokens(dictionary):
    # create list of words that ened sentences
    stop_tokens = []
    for key, value in dictionary.items():
        if key[1] == "STOP":
            stop_tokens.append(key)
    return stop_tokens

def walk(start_token, dictionary):
    # walks the markov
    sentence = ['START', start_token[1]]
    #while the last entry in the list sentence is not "STOP"
    while sentence[len(sentence)-1] != 'STOP': #or len(sentence) < 19:
        window = (sentence[len(sentence) - 2], sentence[len(sentence)-1])
        hist = dictionary[tuple(window)]
        next_word = sample.weighted_random(hist, sample.sum_value(hist))
        sentence.append(next_word)
    return(sentence)

def finalize(sentence):
    # remove start_token and capatlize the second word of the listself.
    sentence.pop(0)
    sentence.pop()
    sentence[0] = sentence[0].capitalize()
    word_string = ''
    word_string = word_string.join(' '+ word for word in sentence) + '.'
    return word_string



if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    words = cleanup.text_list(file1)
    # m_chain = order_mchain(2, words)
    m_chain = m_chain_one(words)
    print(m_chain)
    # c_start = start_token(m_chain)
    # walk_the_dog = walk(c_start, m_chain)
    # print(finalize(walk_the_dog))
