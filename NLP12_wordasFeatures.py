# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:58:04 2018

@author: hp
"""

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print("all words are:" +str(all_words))

word_features = list(all_words.keys())[:3000]
print("word features are:" +str(word_features))

#Mostly the same as before, only with now a new variable, word_features, which contains the top 3,000 most common words. 
#Next, we're going to build a quick function that will find these top 3,000 words in our positive and negative documents, marking their presence as either positive or negative:



def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
#Next, we can print one feature set like:

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
#Then we can do this for all of our documents, saving the feature existence booleans and
# their respective positive or negative categories by doing:

featuresets = [(find_features(rev), category) for (rev, category) in documents]