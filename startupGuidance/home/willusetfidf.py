# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:13:41 2019

@author: Dell
"""


# Making the Uniqueness Function of MDD Model
# Let's get started BITCH!



    # Importing the Libraries
def Uniqueness(idea):
    import numpy as np
    import pandas as pd
    import math


    # Importing the dataset

    dataset = pd.read_csv('C:/Users/abhi/Documents/startupGuidance/startupGuidance/home/startup_funding_1.csv')

    # Cleaning the texts and tf

    import re
    import nltk
        # nltk.download('stopwords')
    from nltk.corpus import stopwords

    corpus = []
    ct = 0
    oc = []
    for i in range(0, 347):
        review = re.sub('[^a-zA-Z]', ' ', dataset['SubVertical'][i])
        review = review.lower()
        review = review.split()
        corpus.append(review)
            # counting numbers
        d = 0
        ct = [0]*len(review)
        for word in review:
            ct[d] = ct[d] + review.count(word)
            d = d + 1
        oc.append(ct)
    for i in range(len(oc)):
        for j in range(len(oc[i])):
            oc[i][j] = oc[i][j]/(len(oc[i]))


    st = idea
    # Getting the Idf Value
    i = 0
    j = 0
    k = 0
    l = 0
    money = 0
    idf1 = []
    no = 0
    for i in range(0, 347):
        idf = [0] * len(corpus[i])
        for j in range(0, len(corpus[i])):
            no = 0
            for k in range(0, 347):
                money = 0
                for l in range(0, len(corpus[k])):
                    if (corpus[i][j] == corpus[k][l]):
                        money = money + 1
                if (money > 0):
                    no = no + 1
            idf[j] = no
        idf1.append(idf)

    i = 0
    j = 0
    for i in range(0, 347):
        for j in range(0, len(corpus[i])):
            idf1[i][j] = math.log((347/idf1[i][j]))

        # Making the TFIDF Model
    i = 0
    j = 0
    ans = []
    yam = 0
    r = st.split()
    for i in range(0, 347):
        for j in range(0, len(oc[i])):
            idf1[i][j] = oc[i][j] * idf1[i][j]

    for k in r:
        yam = 0
        for i in range(0, 347):
            for j in range(0, len(corpus[i])):
                if (k == corpus[i][j]):
                    ans.append(idf1[i][j])
                    yam = 10
                    break
            if (yam == 10):
                break


    # getting average value
    add = 0
    for i in ans:
        add = add + i
    add = add / len(ans)
    return (add)
