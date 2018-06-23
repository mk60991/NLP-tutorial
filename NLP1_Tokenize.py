# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:27:06 2018

@author: hp
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words=set(stopwords.words("english"))
sample_sentence="hii.. how are u??,, what are u doing''..,,"

a=word_tokenize(sample_sentence)

for word in a:
    if word not in stop_words:
        print(word)
        
        
        
        
        
from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
#to tokenize the given text into sentence
print(sent_tokenize(EXAMPLE_TEXT))

#to tokenize the given text into word
print(word_tokenize(EXAMPLE_TEXT))