import tweepy
import pymongo
from pymongo import MongoClient
import json
from credentials import *

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
clientLanguageService = language.LanguageServiceClient()

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
    
def isFromCandidate(tweet):
    us = tweet["user"]
    candidates = ["lopezobrador_", "JoseAMeadeK", "RicardoAnayaC", "Mzavalagc", "JaimeRdzNL"]
    for candidate in candidates:
        if us["screen_name"] == candidate:
            return True
        else:
            usersDic.append(us)
            return False

def saveUsers(users,screen_name):
    for user in users:
        try:
            db["users"+screen_name].insert_one(user)
        except Exception as e:
            print ("there is a problem ", e)
        else:
            print("User Saved")

def saveTweets(tweets, screen_name):
    for tweet in tweets:
        try:
            db['users'+screen_name].insert_one(tweet)
        except Exception as e:
            print("Problem " + e)
        else :
            print("Tweet saved")

def getSentiment(text):
    return clientLanguageService.analyze_sentiment(document=text).document_sentiment


def mineKeyword(keywords, screen_name):
    api = connectionTweepy()
    count = 0
    for keyword in keywords:
        search_results = api.search(q=keyword , count=100)
        print(type(search_results))
        print(len(search_results))
        for tweet in search_results: 
            ##cleaaan
            json_str = json.dumps(tweet._json)
            jsonTweet = json.loads(json_str)
            if not isFromCandidate(jsonTweet) :
                text = jsonTweet["text"]
                print(text)
                clean_text = " ".join(item for item in text.split() if not (item.startswith('@') and len(item) > 2))
                clean_text = " ".join(item for item in clean_text.split() if not (item.startswith('https://') and len(item) > 7))
                clean_text = " ".join(item for item in clean_text.split() if not (item.startswith('R') and item.endswith('T') and len(item) > 1))
                clean_text = " ".join(item for item in clean_text.split() if not (item.startswith('#') and len(item) > 2))

                jsonTweet["clean_text"] = clean_text
                # Detects the sentiment of the text
                sentiment = getSentiment(clean_text)
                print('Text: {}'.format(clean_text))
                print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

                print(jsonTweet)
                count = count + 1
                print(count)

    #saveUsers(usersDic, screen_name)

mineKeyword(keywords["lopezobrador_"], "lopezobrador_")
## get general tweets with at least 5 keywords DONE
## get users of tweets, clean candidates tweets DONE
## validate different user when saving on db DONE
## save users, not candidates
##clean data RT @USER https://
## get tweets with coordenates values
## save gentweets about candidate

## check gentweets if they responses to top10 tweets of candidate (or all candidates tweets)
## save responses to analyze 
