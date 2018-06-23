# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:21:15 2018

@author: hp
"""

import nltk
import random
#C:\Users\hp\AppData\Roaming\nltk_data\corpora\movie_reviews
from nltk.corpus import movie_reviews
#
#Basically, in plain English, the above code is translated to: 
#In each category (we have pos or neg), take all of the file IDs (each review has its own ID), then store the word_tokenized version (a list of words) for the file ID, 
#followed by the positive or negative label in one big list.
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#print out documents[1], which is a big list, where the first element is a list the words, 
#and the 2nd element is the "pos" or "neg" label.
random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#we can perform a frequency distribution, to then find out the most common words. 
print(all_words.most_common(15))
#here we can also find out how many particualar words are occurences in given dataset
print(all_words["stupid"])
print(all_words["sex"])
print(all_words["love"])