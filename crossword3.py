import random
import numpy as np

file = open("/Users/ellie/Downloads/OpenThesaurus-Textversion/openthesaurus.txt","r+")
file = file.read().splitlines()
#for line in file:
#    print(line)

def getword():
    i = random.randint(0,len(file))
    #print(file[i])
    return file[i]

def synstocross(word):
    list_ = []
    words = word.split(";")
    for each in words:
        #print(each.split())
        if len(each.split())==1:
            list_.append(each)
    if len(list_)>=5:
        return list_
    else:
        return synstocross(getword())

def numcrosses1(syns):
    origsyns = syns.copy()
    trylist = []
    trydict = {}
    keyword = max(syns, key=len)
    keylett = random.sample(keyword, len(keyword))
    syns.remove(keyword)
    for letter in keylett:
        done = False
        for word in syns:
            if letter in word:
                trylist.append([letter, word, word.index(letter)])
                syns.remove(word)
                done = True
                break
            if done == True:
                break
    if len(trylist) in range(int(len(keyword)/2.5), int(len(keyword)/1.5)): #otherwise floats
        #print(origsyns)
        #print(syns)
        return [keyword, trylist]
    else:
        return numcrosses1(synstocross(getword()))

def initarray(crossword, keyword, words, middlecolumn):
    array = []
    for i in range(len(keyword)):
        array.append([])
        for j in range(middlecolumn*2):
            array[i].append(' ')
        array[i][middlecolumn] = '*'
    return array

def revealarray(array, keyword):
    for i in range(len(keyword)):
        array[i][len(keyword)] = keyword[i].upper()
    return array

def answer(array, keyword):
    for i in range(len(keyword)):
        print(" ".join(array[i]))

theanswer = [[], ""]

def makearray(crossword):
    keyword = crossword[0]
    words = crossword[1]
    #print("here: ", keyword,words)
    middlecolumn = len(keyword)
    array = initarray(crossword, keyword, words, middlecolumn)
    copyword = list(keyword)
    for word in words:
        for i in keyword:
            if i == word[1][word[2]]:
                #print(word, word[1], word[1][word[2]])
                wordstart = middlecolumn-word[2]
                wordend = wordstart + len(word[1])
                #print("start ", wordstart, "end ", wordend)
                wordindex = 0
                for k in range(wordstart, wordend):
                    array[copyword.index(i)][k] = word[1][wordindex]
                    #print(array[keyword.index(i)][k])
                    wordindex += 1
                copyword[copyword.index(i)] = 5
                break
    for i in range(len(keyword)):
        print(" ".join(array[i]))
    global theanswer
    revealarray(array, keyword)
    theanswer = [array, keyword]
    #print(copyword)
    #return array

def spiel():
    synsarg = synstocross(getword())
    # print("synsarg: ", synsarg)
    arg = numcrosses1(synsarg)
    # print("arg: ", arg)
    makearray(arg)
    if input("enthüllen? ") == "y":
        answer(theanswer[0], theanswer[1])
        if input("nochmal? ") == "y":
            spiel()
spiel()
