# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:09:52 2018

@author: hp
#"""
#One of the most major forms of chunking in natural language processing is called "Named Entity Recognition." 
#The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations, monetary figures, and more.
#
#This can be a bit of a challenge, but NLTK is this built in for us. 
#There are two major options with NLTK's named entity recognition: either recognize all named entities, or recognize named entities as their respective type, like people, places, locations, etc.

# you can see a few things. When Binary is False, it picked up the same things, 
# but wound up splitting up terms like White House into "White" and "House" as if they were different, 
# whereas we could see in the binary = True option, 
# the named entity recognition was correct to say White House was part of the same named entity.



#if binary='True'
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()





#if binary='false'

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            namedEnt.draw()
    except Exception as e:
        print(str(e))


process_content()