import tweepy, time
#from credentials import *

from os import environ
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search = 'list:Rowdy_Bot/DVS include:nativeretweets'

for tweet in tweepy.Cursor(api.search, search).items():
    tweet.retweet()
    time.sleep(600)
