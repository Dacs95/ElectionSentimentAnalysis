import tweepy
import pymongo
from pymongo import MongoClient
import json
from credentials import *

#Connection to mongo Atlas DataBase
client = MongoClient("mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/")
db = client["sa-data"]
["lopezobrador_","JoseAMeadeK","RicardoAnayaC","Mzavalagc","JaimeRdzNL"]
keywords = {
    'lopezobrador_': ["amlo", "lopez obrador", "@lopezobrador_", "peje", "amlove", "#amlo", "morena", "#morena" ], 
    'JoseAMeadeK': ["meade", "pri", "jose antonio meade", "#primeade", "pri meade", "#meade", "#pri", "pri meade"], 
    'RicardoAnayaC': ["anaya", "ricardo anaya", "pan", "#pan", "#ricardoanaya", "#anaya", "pan anaya" ], 
    'Mzavalagc': [],
    'JaimeRdzNL': [] }

def connectionTweepy():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    return api

def mineKeyword(keywords):
    
    for keyword in keywords[]
    results = api.search(q="lopez obrador" , rpp=100, page=1)
    for result in results: 
        print(result.text)

    api = connectionTweepy()



## get general tweets with at least 5 keywords
## get users of tweets, clean candidates tweets
## get tweets with coordenates values
## save gentweets about candidate

## check gentweets if they responses to top10 tweets of candidate (or all candidates tweets)
## save responses to analyze 
