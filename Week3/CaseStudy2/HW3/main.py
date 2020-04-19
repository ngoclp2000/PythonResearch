# DO NOT EDIT THIS CODE!
import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    text   = pd.read_csv(title_path, sep = "\n", engine='python', encoding="utf8")
    text = text.to_string(index = False)
    return text

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
# #Ex2:
hamlets = pd.read_csv("..../FileCSV/hamlets.csv", 
                      index_col=0)
print(hamlets)
language, text = hamlets.iloc[2]
#Ex3:
# def getLength(list_count):
#     length_return = []
#     for count in list_count:
#         if count > 10:
#             length_return.append("frequent")
#         elif count == 1:
#             length_return.append("unique")
#         else:
#             length_return.append("infrequent")
#     return list(length_return)

# counted_text = count_words_fast(text)
# data = pd.DataFrame({'word': list(counted_text.keys()), 
# 					 'count': list(counted_text.values()),
#                      'frequency': getLength(counted_text.values())})
# data['length'] = data['word'].apply(len)
# subdat = pd.DataFrame({'language': language,
#                         'frequency': ["frequent","infrequent","unique"],
#                         'mean_word_length': data.groupby(by = "frequency")["length"].mean(),
#                         'num_words':data.groupby(by = "frequency").size()})
# print(subdat)

#Ex5
def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    data["length"] = data["word"].apply(len)
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
grouped_data = pd.DataFrame(columns = [
		"language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
# print(grouped_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
print(grouped_data)
plt.show()