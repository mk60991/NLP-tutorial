# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:47:41 2018

@author: hp
"""

#sentence tokenizer, called the PunktSentenceTokenizer.This tokenizer is capable of unsupervised machine learning, 
#so you can actually train it on any body of text that you use
#One of the more powerful aspects of the NLTK module is the Part of Speech tagging that it can do for you. 
#This means labeling words in a sentence as nouns, adjectives, verbs...etc.
#Even more impressive, it also labels by tense, and more.
#

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
#One is a State of the Union address from 2005, and the other is from 2006 from past President George W. Bush.
#Next, we can train the Punkt tokenizer like:

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
#Then we can actually tokenize, using:

tokenized = custom_sent_tokenizer.tokenize(sample_text)
#Now we can finish up this part of speech tagging script by creating a function that will run through and
#tag all of the parts of speech per sentence like so:

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()