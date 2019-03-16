import tweepy
import time

from os import environ
consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token = environ['TWITTER_ACCESS_TOKEN_KEY']
access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search = 'list:Rowdy_Bot/DVS include:nativeretweets'

for tweet in tweepy.Cursor(api.search, search).items():
    try:
        tweet.retweet()
        time.sleep(600)
    except tweepy.TweepError:
        time.sleep(600)
        continue
    except StopIteration:
        break
