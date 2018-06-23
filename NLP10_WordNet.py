# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:34:07 2018

@author: hp
"""
#to access wordnet directory
#C:\Users\hp\AppData\Roaming\nltk_data\corpora\wordnet
#
#WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus.
#You can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more
1.

from nltk.corpus import wordnet
#Then, we're going to use the term "program" to find synsets like so:

syns = wordnet.synsets("program")
#An example of a synset:

print(syns[1].name())

#Just the word:
print(syns[0].lemmas()[0].name())

#Definition of that first synset:
print(syns[0].definition())

#Examples of the word in use:
print(syns[0].examples())



2.

from nltk.corpus import wordnet
#Next, how might we discern synonyms and antonyms to a word? 
#The lemmas will be synonyms, and then you can use .antonyms to find the antonyms to the lemmas

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

3.

#Next, we can also easily use WordNet to compare the similarity of two words and their tenses, 
from nltk.corpus import wordnet

#similarity in percentage

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))