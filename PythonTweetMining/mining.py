import tweepy
import pandas as pd  
import numpy as np
import json
from credentials import *
from IPython.display import display

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
#public_tweets = api.home_timeline()
# foreach through all tweets pulled
#for tweet in public_tweets:
#    print tweet.text

name = "jumarogu"
tweetCount = 100
# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
#for tweet in results:
   #Using panda to manage the data easily 
data = pd.DataFrame(data=[tweet.text for tweet in results], columns=['Tweets'])
data['len']  = np.array([len(tweet.text) for tweet in results])
data['ID']   = np.array([tweet.id for tweet in results])
data['Date'] = np.array([tweet.created_at for tweet in results])
data['Source'] = np.array([tweet.source for tweet in results])
data['Likes']  = np.array([tweet.favorite_count for tweet in results])
data['RTs']    = np.array([tweet.retweet_count for tweet in results])
#   printing the text stored inside the tweet object
#   parsed = json.loads(tweet)
#   print "Usr_ID " + tweet.user.id 
#   print "Name: " + tweet.user.name
#   print "Source: " + tweet.source
#   print "Location: " + tweet.user.location
#   print "Text : " + tweet.text
#   print tweet.user.favourites_count   
#   print tweet.created_at

# We display the first 10 elements of the dataframe:
display(data.head(10))

