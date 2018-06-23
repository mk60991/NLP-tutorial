# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:16:06 2018

@author: hp
"""
#C:\Users\hp\Anaconda3\Lib\site-packages\textblob
from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki)
print(wiki.words)
print(wiki.sentences)





from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
#Create a TextBlob
blob1 = TextBlob(text)
#Part-of-speech Tagging¶
print(blob1.tags)          
#Noun Phrase Extraction
print(blob1.noun_phrases )

#sentiment analysis
for sentence in blob1.sentences:
    print(sentence.sentiment.polarity)
#to translate in any language 
    #TRANSLATION  works on INTERNET CONNECTION
print(blob1.translate(to="es"))
#to split the text into words
print(blob1.words)
#to split text into sentences
print(blob1.sentences)


#The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity).
# The polarity score is a float within the range [-1.0, 1.0]. 
# The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)



#Tokenization
# break TextBlobs into words or sentences.

zen = TextBlob("Beautiful is better than ugly. "
               "Explicit is better than implicit. "
               "Simple is better than complex.")
print(zen.words)
print(zen.sentences)

for sentence in zen.sentences:
    print(sentence.sentiment)
    
    
#Words Inflection and Lemmatization
    
#word Inflection
sentence = TextBlob('Use 4 spaces per indentation level.')
print(sentence.words)
print(sentence.words[2].singularize())
print(sentence.words[-1].pluralize())


#Words can be lemmatized by calling the lemmatize method.

from textblob import Word
w1 = Word("octopi")
print(w1.lemmatize())
w2 = Word("went")
print(w2.lemmatize("v"))


#WordNet Integration
#access the synsets for a Word via the synsets property or the get_synsets method, optionally passing in a part of speech.

from textblob import Word
from textblob.wordnet import VERB
word1 = Word("octopus")
print(word1.synsets)
Word("hack").get_synsets(pos=VERB)

#access the definitions for each synset via the definitions property or the define()
Word("octopus").definitions
Word("hack").define()


#WordLists
#A WordList is just a Python list with additional methods.
from textblob import TextBlob

animals = TextBlob("cat dog octopus")
print(animals.words)

print(animals.words.pluralize())

#spelling correction
#Use the correct() method to attempt spelling correction.

b = TextBlob("I havv goood speling!")
print(b.correct())


#Word objects have a spellcheck() Word.spellcheck() method that returns a list of (word, confidence) tuples with spelling suggestions.
from textblob import Word
w1 = Word('falibility')
print(w1.spellcheck())

w2= Word('pluralize')
print(w2.spellcheck())



#Get Word and Noun Phrase Frequencies
#There are two ways to get the frequency of a word or noun phrase in a TextBlob.
#
#The first is through the word_counts dictionary.

monty = TextBlob("We are no longer the Knights who say Ni. "
                 "We are now the Knights who say Ekki ekki ekki PTANG.")
print(monty.word_counts['ekki'])

#The second way is to use the count() method.

print(monty.words.count('who'))

#specify whether or not the search should be case-sensitive (default is False).
print(monty.words.count('Knights', case_sensitive=True))


#TRANSLATOR WORKS ON INTERNET CONNECTION

#Translation and Language Detection
#TextBlobs can be translated between languages.

en_blob = TextBlob(u'Simple is better than complex.')
en_blob.translate(to='es')

#If no source language is specified, TextBlob will attempt to detect the language. 
#You can specify the source language explicitly, like so. 
#Raises TranslatorError if the TextBlob cannot be translated into the requested language or NotTranslated 
#if the translated result is the same as the input string.
chinese_blob = TextBlob(u"美丽优于丑陋")
chinese_blob.translate(from_lang="zh-CN", to='en')


#also attempt to detect a TextBlob’s language using TextBlob.detect_language().

b = TextBlob(u"بسيط هو أفضل من مجمع")
b.detect_language()



#Parsing
#Use the parse() method to parse the text.

b = TextBlob("And now for something completely different.")
print(b.parse())



#TextBlobs Are Like Python Strings!
#You can use Python’s substring syntax.
zen = TextBlob("Beautiful is better than ugly. "
               "Explicit is better than implicit. "
               "Simple is better than complex.")


zen[0:19]
TextBlob("Beautiful is better")

print(zen.upper())
print(zen.find("Simple"))


#make comparisons between TextBlobs and strings.

apple_blob = TextBlob('apples')
banana_blob = TextBlob('bananas')
print(apple_blob < banana_blob)
print(apple_blob == 'apples')



#n-grams
#The TextBlob.ngrams() method returns a list of tuples of n successive words.
blob = TextBlob("Now is better than never.")
print(blob.ngrams(n=3))



#Get Start and End Indices of Sentences
#Use sentence.start and sentence.end to get the indices where a sentence starts and ends within a TextBlob.

for s in zen.sentences:
    
    print(s)
    print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))