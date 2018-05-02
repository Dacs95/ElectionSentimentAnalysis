import tweepy
import pandas as pd  
import numpy as np
import pymongo
from pymongo import MongoClient
import json
from credentials import *
import json
from IPython.display import display
import ast

#Connection to mongo Atlas DataBase cluster0-y8r2m.mongodb.net
client = MongoClient("mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/")
db = client["sa-data"]

# Creating the authentication object
# Setting your access token and secret
# Creating the API object while passing in auth information
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 

usuario = {"name":"juan",
            "situation":"horrible"
}
#db.persona.insert_one({"name":"juan", "situation":"horrible"})

name = 'lopezobrador_'
tweetCount = 100
results = api.user_timeline(id=name, count=tweetCount)

def populares(favourites , retweets):
    prom = (favourites + retweets * 2)/2
    return prom

#Check every tweet in the results array
for x in range(0,len(results)):
    try:
        #Calculate the popularityAverage
        avg = populares(results[x].favorite_count,results[x].retweet_count)
        json_str = json.dumps(results[x]._json)
        jsonTweet = json.loads(json_str)
        jsonTweet['popularity']  =  avg
        print(jsonTweet['id'])

        #Save tweets in the database
        #db["tweets-lopezobrador_"].insert_one(jsonTweet)
        
    except Exception as e:
        print ("there is a problem ", e) 
    else:
        print ("inserted")

#top10
lopezTimelineCollection = db["tweets-lopezobrador_"]
top10 = lopezTimelineCollection.find().sort([('popularity',-1)]).limit(10)
#db['top-lopezobrador_'].insert_many(top10)
for results in top10: 
    print(results["id"])

results = api.search(q="lopez obrador" , rpp=100, page=1)

for result in results: 
    print(result.text)