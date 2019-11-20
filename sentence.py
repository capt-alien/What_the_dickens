from sys import argv
import cleanup
import tokenize
import wordcount
import sample



def sentance(histogram, total, loop):
    looper = int(loop)
    sentance1= []
    word_string = " "
    # loop
    for i in range(0,looper):
        weight_word = sample.weighted_random(histogram, total)
        sentance1.append(weight_word)
    #turn list into a string
    word_string = word_string.join(word for word in sentance1)
    return word_string

if __name__ == '__main__':
    file1 = argv[1]  #file to analyze
    looper = int(argv[2]) # number of times that loop will run
    hist1 = wordcount.dict_words((cleanup.text_list(file1)))
    total = wordcount.sum_value(hist1)
    #runs sentance function
    print(sentance(hist1, total, looper))
