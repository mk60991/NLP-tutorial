# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:30:04 2018

@author: hp
"""

#Now that we know the parts of speech, we can do what is called chunking, and
# group words into hopefully meaningful chunks. 
# One of the main goals of chunking is to group into what are known as "noun phrases." 
# These are phrases of one or more words that contain a noun, maybe some descriptive words, maybe a verb,
# and maybe something like an adverb. 
#The idea is to group nouns with the words that are in relation to them.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

#<RB.?>* = "0 or more of any tense of adverb," followed by:
#<VB.?>* = "0 or more of any tense of verb," followed by:
#<NNP>+ = "One or more proper nouns," followed by
#<NN>? = "zero or one singular noun."

#here form loop of tree of chunk
def process_content():
    try:
#        for i in tokenized:
#            words = nltk.word_tokenize(i)
#            tagged = nltk.pos_tag(words)
#            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#            chunkParser = nltk.RegexpParser(chunkGram)
#            chunked = chunkParser.parse(tagged)
#            chunked.draw()   
        for subtree in chunked.subtrees():
                print(subtree)

        

    except Exception as e:
        print(str(e))
   
process_content()







import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#C:\Users\hp\AppData\Roaming\nltk_data\corpora\state_union\2005-GWBush
#C:\Users\hp\AppData\Roaming\nltk_data\corpora\state_union\2006-GWBush
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()
