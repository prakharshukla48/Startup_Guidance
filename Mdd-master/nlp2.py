# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:55:08 2019

@author: Dell
"""


# NLP

# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the TFIDF Model
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features = 1500)
X = tfidf.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
