from sys import argv
import cleanup
import sample
import sentence
import dictogram
import random

def m_chain_one(text_list):
    markov_dict = {}
    for index in range(len(text_list) - 1):
        window = text_list[index]
        if index in markov_dict:
            markov_dict[window].add_count([text_list[index + 1]])
        else:
            markov_dict[window] = dictogram.Dictogram([text_list[index + 1]])
    return markov_dict

#nth Order markov Chain derived from first order
def order_mchain(order, text_list):
    markov_dict = {}
    for index in range(len(text_list) - order):
        window = tuple(text_list[index: index + order])
        if window in markov_dict:
            markov_dict[window].add_count([text_list[index + order]])
        else:
            markov_dict[window] = dictogram.Dictogram([text_list[index + order]])
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
    stop_tokens = []
    for key, value in dictionary.items():
        if key[1] == "STOP":
            stop_tokens.append(key)
    return stop_tokens

def walk(start_token, dictionary):
    sentence = ['START', start_token[1]]
    while sentence[len(sentence)-1] != 'STOP': #or len(sentence) < 19:
        window = (sentence[len(sentence) - 2], sentence[len(sentence)-1])
        hist = dictionary[tuple(window)]
        next_word = sample.weighted_random(hist, sample.sum_value(hist))
        sentence.append(next_word)
    return(sentence)

def finalize(sentence):
    sentence.pop(0)
    sentence.pop()
    sentence[0] = sentence[0].capitalize()
    word_string = ''
    word_string = word_string.join(' '+ word for word in sentence) + '.'
    return word_string

def main():
        file1 = argv[1]
        words = cleanup.text_list(file1)
        m_chain = order_mchain(2, words)
        print(m_chain)

if __name__ == '__main__':
    main()
