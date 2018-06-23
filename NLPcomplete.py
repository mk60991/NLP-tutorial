# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:17:55 2018

@author: hp
"""

from bs4 import BeautifulSoup
#use the urllib module to crawl the web page:
 
import urllib.request
 
response = urllib.request.urlopen('http://php.net/')
#a lot of HTML tags 
html = response.read()
#print(html)
#BeautifulSoup to clean the grabbed text
soup = BeautifulSoup(html,"html5lib")
#print(soup)
# clean text from the crawled web page 
text = soup.get_text(strip=True)
 #print (text)

# convert that text into tokens by splitting the text
tokens = [t for t in text.split()]
#print (tokens)

#count word frequency
#There is a function in NLTK called FreqDist() does the job:
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
  print (str(key) + ':' + str(val))

#If you search the output, we’ll find that the most frequent token is PHP.
#plot a graph for those tokens using plot function 
freq.plot(40, cumulative=False)


#here are some words like The, Of, a, an, and so on. These words are stop words.
#Generally, stop words should be removed to prevent them from affecting our results.

#NLTK is shipped with stop words lists for most languages. To get English stop words, 
from nltk.corpus import stopwords
stop1=stopwords.words('english')
print("list of possible stopwords:" +str(stop1))

#make a copy of the list, then we will iterate over the tokens and remove the stop words:
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
 
        clean_tokens.remove(token)
        
        
        
        
        
        
        
#        
#We saw how to split the text into tokens using split function, 
#now we will see how to tokenize the text using NLTK.
#Tokenizing text is important since text can’t be processed without tokenization. 
#Tokenization process means splitting bigger parts to small parts.
#
#You can tokenize paragraphs to sentences and tokenize sentences to words according to your needs.
# NLTK is shipped with sentence tokenizer and word tokenizer.
        
        #sentence Tokenizer
from nltk.tokenize import sent_tokenize
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))

#from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(word_tokenize(mytext))


#To tokenize other languages, you can specify the language
from nltk.tokenize import sent_tokenize
mytext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(mytext,"french"))


#WordNet is a database which is built for natural language processing. 
#It includes groups of synonyms and a brief definition.
from nltk.corpus import wordnet
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())


from nltk.corpus import wordnet
syn = wordnet.synsets("NLP")
print(syn[0].definition())
 
syn1 = wordnet.synsets("Python")
print(syn1[2].definition())




#WordNet to get synonymous words like this:
from nltk.corpus import wordnet
synonyms = []
for syn in wordnet.synsets('Computer'):
 
    for lemma in syn.lemmas():
 
        synonyms.append(lemma.name())
 
print(synonyms)

#get antonyms from wordnet
from nltk.corpus import wordnet
antonyms = []
for syn in wordnet.synsets("small"):
 
    for l in syn.lemmas():
 
        if l.antonyms():
 
            antonyms.append(l.antonyms()[0].name())
 
print(antonyms)


#
#Word stemming means removing affixes from words and return the root word. Ex: The stem of the word working => work.
#Search engines use this technique when indexing pages, so many people write different versions for the same word and all of them are stemmed to the root word.
#There are many algorithms for stemming, but the most used algorithm is Porter stemming algorithm.
#NLTK has a class called PorterStemmer which uses Porter stemming algorithm.
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))
#0r
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('increases'))



#Lemmatizing Words Using WordNet
#Word lemmatizing is similar to stemming, but the difference is the result of lemmatizing is a real word.
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))


#the default part of speech is nouns. To get'v' verbs, you should specify it like this:

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing', pos="v"))


#result could be a verb, noun, adjective, or adverb:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing', pos="v"))
print(lemmatizer.lemmatize('playing', pos="n"))
print(lemmatizer.lemmatize('playing', pos="a"))
print(lemmatizer.lemmatize('playing', pos="r"))

#
#Stemming and Lemmatization Difference
#OK, let’s try stemming and lemmatization for some words:

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

lemmatizer = WordNetLemmatizer()

print(stemmer.stem('stones'))

print(stemmer.stem('speaking'))

print(stemmer.stem('bedroom'))

print(stemmer.stem('jokes'))

print(stemmer.stem('lisa'))

print(stemmer.stem('purple'))

print('----------------------')

print(lemmatizer.lemmatize('stones'))

print(lemmatizer.lemmatize('speaking'))

print(lemmatizer.lemmatize('bedroom'))

print(lemmatizer.lemmatize('jokes'))

print(lemmatizer.lemmatize('lisa'))

print(lemmatizer.lemmatize('purple'))

#Stemming works on words without knowing its context and that’s why stemming has lower accuracy and faster than lemmatization.
#
#In my opinion, lemmatizing is better than stemming. Word lemmatizing returns a real word even 
#if it’s not the same word, it could be a synonym, but at least it’s a real word.
#
#Sometimes you don’t care about this level of accuracy and 
#all you need is speed, in this case, stemming is better.
