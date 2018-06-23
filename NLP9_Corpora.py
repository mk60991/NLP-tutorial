# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:21:37 2018

@author: hp
"""
C:\Users\yourname\AppData\Roaming\nltk_data\corpora

Within here, you have all of the available corpora, including things like books, chat logs, movie reviews, and a whole lot more.
Now, we're going to talk about accessing these documents via NLTK. 
As you can see, these are mostly text documents, so you could just use normal Python code to open and read documents. 
That said, the NLTK module has a few nice methods for handling the corpus, 
so you may find it useful to use their methology.
Here's an example of us opening the Gutenberg Bible, and reading the first few lines:



from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

# sample text
#C:\Users\hp\AppData\Roaming\nltk_data\corpora\gutenberg\bible-kjv.txt
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])