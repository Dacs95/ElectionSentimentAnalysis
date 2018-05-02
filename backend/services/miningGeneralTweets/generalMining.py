import tweepy
import pymongo
from pymongo import MongoClient
import json
from credentials import *

usersDic = []
#Connection to mongo Atlas DataBase
client = MongoClient("mongodb+srv://Dacs95:blanco12@cluster0-y8r2m.mongodb.net/")
db = client["sa-data"]
tweets = {}

keywords = {
    'lopezobrador_': ["amlo", "lopez obrador", "@lopezobrador_", "peje", "#amlove", "#amlo", "morena", "#morena", "amlono", "amlove"], 
    'JoseAMeadeK': ["meade", "pri", "jose antonio meade", "@JoseAMeadeK", "#primeade", "pri meade", "#meade", "#pri", "pri meade", "#yomero", "#avanzarcontigo"], 
    'RicardoAnayaC': ["anaya", "ricardo anaya", "@RicardoAnayaC", "pan", "#pan", "#ricardoanaya", "#anaya", "pan anaya", "#prian", "#conanayapormexico", "#defrentealfuturo"], 
    'Mzavalagc': ["margarita", "independiente", "@Mzavalagc", "#MargaritaNosConvieneATODOS", "margarita zavala", "maz", "calderon-zavala", "la señora calderon", "zabala"], 
    'JaimeRdzNL': ["bronco", "@JaimeRdzNL", "jaime rodriguez", "cortele la mano", "jaime rodriguez calderon", "candidato independiente", "#levantatemexico", "#mexicobronco"] 
    }

def connectionTweepy():
    # Creating the authentication object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # Setting your access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # Creating the API object while passing in auth information
    api = tweepy.API(auth)
    return api
    
def isFromCandidate(tweet, id):
    us = tweet["user"]
    if us["screen_name"] == id:
        return True
    else:
        usersDic.append(us)
        return False

def saveUsers(users,name):
    for user in users:
        try:
            db["users-"+name].insert_one(user)
        except expression as identifier:
            print ("there is a problem ",e)
        else:
            print("User Saved Wiiiiii XDXDXD me vale verga a la verga")
    

def mineKeyword(keywords):
    api = connectionTweepy()
    for keyword in keywords:
        search_results = api.search(q=keyword , count=100)
        print(type(search_results))
        print(len(search_results))
        for tweet in search_results: 
            ##cleaaan
            #if(!fromCandidate(tweet))
            json_str = json.dumps(tweet._json)
            jsonTweet = json.loads(json_str)
            print(jsonTweet['text'])

mineKeyword(["amlo"])
## get general tweets with at least 5 keywords
## get users of tweets, clean candidates tweets
## validate different user when saving on db
## get tweets with coordenates values
## save gentweets about candidate

## check gentweets if they responses to top10 tweets of candidate (or all candidates tweets)
## save responses to analyze 
