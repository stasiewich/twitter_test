# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:18:21 2022

@author: pstasiewich
"""

# Import the necessary libraries
import tweepy
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st 
import streamlit.components.v1 as components
import requests


# Set the API keys
consumer_key = 'aD7Jbh8y3wPiYIQ4okaHQ6719'
consumer_secret = 'XKZS37C8B5XTyZLoNVwlkoiQN37Cs8Lf1H7CluKY58ejf5IgGq'
access_token = '1600549558223880206-anZWHvrafrUdTdVmttTT689npPLzWK'
access_token_secret = 'Hgnx9rfmh6cjmeZYEEGevQ13r1cvRhl9ezIJjuPLJJwwK'

# Authenticate your API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Create URL to append tweet ID to
tweet_url = 'https://twitter.com/twitter/status/'

# Set the search term and the date range
# Set to T-1 Month
search_term = 'Edmonton Oilers'
date_since_range = datetime.now() - relativedelta(months=1)
date_since = date_since_range.strftime('%Y-%m-%d')
print(date_since)

# Perform the search
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_term,
                       lang='en',
                       since_id=date_since).items(5)

# Iterate over the tweets and print their text
tweet_results = []

for tweet in tweets:
    tweet_id = str(tweet.id)
    final_url = tweet_url+tweet_id
    tweet_results.append(final_url)

def theTweet(tweet_results):
    
    tweet_html = []
    
    for result in tweet_results:
        api = "https://publish.twitter.com/oembed?url={}".format(result)
        response = requests.get(api)
        res = response.json()["html"] 
        tweet_html.append(res)
        
    return(tweet_html)

res = theTweet(tweet_results)

with st.expander("Load live feed"):
  st.write("Tag rink using #RinkName to provide real time updates on conditions, games, etc.")
  for tweet in res:
      components.html(tweet)
      st.test = components.html(tweet, height=300, scrolling=True)
