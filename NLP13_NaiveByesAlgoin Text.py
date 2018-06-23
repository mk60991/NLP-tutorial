# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:02:40 2018

@author: hp
"""


import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print("all words are:" +str(all_words))

word_features = list(all_words.keys())[:3000]
print("word features are:" +str(word_features))

#Mostly the same as before, only with now a new variable, word_features, which contains the top 3,000 most common words. 
#Next, we're going to build a quick function that will find these top 3,000 words in our positive and negative documents, marking their presence as either positive or negative:



def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
#Next, we can print one feature set like:

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
#Then we can do this for all of our documents, saving the feature existence booleans and
# their respective positive or negative categories by doing:

featuresets = [(find_features(rev), category) for (rev, category) in documents]
#
# The algorithm that we're going to use first is the Naive Bayes classifier. 
# This is a pretty popular algorithm used in text classification, 
# so it is only fitting that we try it out first. Before we can train and test our algorithm, however,
# we need to go ahead and split up the data into a training set and a testing set.
#ou could train and test on the same dataset, but this would present you with some serious bias issues, 
#so you should never train and test against the exact same data. To do this, since we've shuffled our data set, we'll assign the first 1,900 shuffled reviews, consisting of both positive and negative reviews, 
#as the training set. Then, we can test against the last 100 to see how accurate we are.
#
#This is called supervised machine learning, because we're showing the machine data, and telling it "hey, 
#this data is positive," or "this data is negative." Then, after that training is done, 
#we show the machine some new data and ask the computer, based on what we taught the computer before, what the computer thinks the category of the new data is



# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]
#Next, we can define, and train our classifier like:

classifier = nltk.NaiveBayesClassifier.train(training_set)
#First we just simply are invoking the Naive Bayes classifier, then we go ahead and use .train() to train it all in one line.

#asy enough, now it is trained. Next, we can test it:

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)


#
#use the Pickle module to go ahead and serialize our classifier object, 
#so that all we need to do is load that file in real quick.
#So, how do we do this? The first step is to save the object.
import pickle
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# opens up a pickle file, preparing to write in bytes some data.
# Then, we use pickle.dump() to dump the data. The first parameter to pickle.dump() is what are you dumping, 
# the second parameter is where are you dumping it.
#
#classifier_f = open("naivebayes.pickle", "rb")
#classifier = pickle.load(classifier_f)
#classifier_f.close()
