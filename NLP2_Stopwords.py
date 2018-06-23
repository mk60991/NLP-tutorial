# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:19:52 2018

@author: hp
"""
# In natural language processing, useless words (data), are referred to as stop words.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sent = "This is a sample sentence, showing off the stop words filtration."

#set stopwords in 'english' it contain list of possible stopwords
#that is used to refine the sentences
#using the stop_words set to remove the stop words from your text:
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)