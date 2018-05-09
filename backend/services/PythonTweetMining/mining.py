import tweepy
import pymongo
from pymongo import MongoClient
import json
from credentials import *

#Connection to mongo Atlas DataBase
client = MongoClient("mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/")
db = client["sa-data"]

def connectionTweepy():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    return api

def mine(id_name, tweetCount):
    #Geting a reference to the tweepy api
    api = connectionTweepy()
    # Calling the user_timeline function with our parameters
    results = api.user_timeline(id=id_name, count=tweetCount)
    return results

def populares(favourites , retweets):
    prom = (favourites + retweets * 2)/2
    return prom

def top10(name):
    lista = db["tweets-"+name].find().sort([('popularity',-1)]).limit(10)
    return lista

def saveTop10(top, name):
    for x in range(0,10):
        try:
            db["top-"+name].insert_one(top[x])
        except Exception as e:
            print ("there is a problem ",e) 
        else:
            print ("Top Saved") 

#name of the account you want a mine
candidatos = ["lopezobrador_","JoseAMeadeK","RicardoAnayaC","Mzavalagc","JaimeRdzNL"]
#number of tweets you want
tweetCount = 100
for c in range(0,len(candidatos)):
    #Mine the timeline of a specific user
    tweets = mine(candidatos[c],tweetCount)
    #Check every tweet in the results array
    for tweet in tweets:
        try:
            #Calculate the popularityAverage
            avg = populares(tweet.favorite_count,tweet.retweet_count)
            json_str = json.dumps(tweet._json)
            jsonTweet = json.loads(json_str)
            jsonTweet['popularity'] = avg

            #Save tweets in the database
            db["tweets-"+candidatos[c]].insert_one(jsonTweet)
        
        except Exception as e:
            print ("there is a problem ",e) 
        else:
            print ("inserted")

    topTweets = top10(candidatos[c])
    saveTop10(topTweets,candidatos[c])
    
