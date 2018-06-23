# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:35:47 2018

@author: hp
"""
#
#The idea of stemming is a sort of normalizing method.
#Many variations of words carry the same meaning, other than when tense is involved.
#The reason why we stem is to shorten the lookup, and normalize sentences.

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]


for w in example_words:
    print(ps.stem(w))





from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
