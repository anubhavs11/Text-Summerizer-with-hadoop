#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:29:02 2018

@author: root
"""

import re
import nltk
import heapq
import sys

text = ""

dataset = sys.stdin

for data in dataset:
    text += str(data)

text = re.sub(r"\[[0-9]*\]"," ",text)
text = re.sub(r"\s+"," ",text)
 
clean_text = text.lower()
clean_text = re.sub(r"\W"," ",clean_text)
clean_text = re.sub(r"\d"," ",clean_text)
clean_text = re.sub(r"^\s","",clean_text)
clean_text = re.sub(r"\s$","",clean_text)
clean_text = re.sub(r"\s+"," ",clean_text)

sentences = nltk.sent_tokenize(text)
stop_words = nltk.corpus.stopwords.words("english")

# CREATING HISTOGRAM

word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

#CREATING WIGHTED HISTOGRAM
            
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())
    
# CALCULATING SENTENCE SCORES
    
sent2score = {}

for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 30:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] += word2count[word]
                    
best_sentences = heapq.nlargest(5,sent2score,key = sent2score.get)

for sentence in best_sentences:
    print(sentence)    
