import os
from collections import Counter
import pandas as pd
def countWords(text):
    text = text.lower()
    skips = [",",".",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")
    word_count ={}
    for word in text.split(" "):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def readBook(title_book):
    with open(title_book,"r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

def wordStats(word_count):
    num_unique = len(word_count)
    counts = word_count.values()
    return (num_unique, counts)

book_dir = "../Books"
stats = pd.DataFrame(columns = ("language","author","title" , "length","unique"))
title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author ):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            text = readBook(inputfile)
            (num_unique, counts) = wordStats(countWords(text))
            stats.loc[title_num] = language , author, title , sum(counts) , num_unique
            title_num += 1
print(stats.length)    