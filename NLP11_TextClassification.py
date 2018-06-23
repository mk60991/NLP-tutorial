# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:43:12 2018

@author: hp
"""







import nltk
import random
from nltk.corpus import movie_reviews
#
#Basically, in plain English, the above code is translated to:
#In each category (we have pos or neg), take all of the file IDs (each review has its own ID), 
#then store the word_tokenized version (a list of words) for the file ID,
#followed by the positive or negative label in one big list.
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#Next, we use random to shuffle our documents. This is because we're going to be training and testing. 
#If we left them in order, chances are we'd train on all of the negatives, some positives,
#and then test only against positives
random.shuffle(documents)

#Then, just so you can see the data you are working with, we print out documents[1], 
#which is a big list, where the first element is a list the words, and the 2nd element is the "pos" or "neg" label.
print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#we want to collect all words that we find, so we can have a massive list of typical words. From here, 
#we can perform a frequency distribution, to then find out the most common words. 

print(all_words.most_common(15))
#The above gives you the 15 most common words. 
#find out how many occurences a word has by doing:

print(all_words["stupid"])