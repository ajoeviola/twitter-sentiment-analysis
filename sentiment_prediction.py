import numpy as np
import pandas as pd
import json 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def predict_sentiment():
    #creating an object of sentiment intensity analyzer
    sia= SentimentIntensityAnalyzer()
    data = pd.DataFrame(columns = ["compound", "negative", "positive", "classification"])

    f = open('tweets.json')
    tweets = json.load(f)

    #postcontent = []

    for tweet in tweets:
        result = sia.polarity_scores(tweet["content"])
        compound = result['compound']
        negative = result['neg']
        positive = result['pos']
        if compound > 0:
            classification = 'positive'
        elif compound < 0:
            classification = 'negative'
        else:
            classification = 'neutral'

        #append our new tweet to the dataframe
        data.loc[len(data.index)] = [compound, negative, positive, classification]


    #num_positive = data['classification'].value_counts()['positive']
    #num_negative = data['classification'].value_counts()['negative']
    #num_neutral = data['classification'].value_counts()['neutral']

    return data

    #print("positive tweets:", num_positive)
    #print("negative tweets:", num_negative)
    #print("neutral tweets:", num_neutral)


