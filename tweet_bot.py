import tweepy, time
from credentials import *

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search = 'list:Rowdy_Bot/DVS include:nativeretweets'

for tweet in tweepy.Cursor(api.search, search).items():
    tweet.retweet()
    time.sleep(600)