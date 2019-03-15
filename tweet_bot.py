import tweepy, time
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search = 'list:Rowdy_Bot/DVS include:nativeretweets'

for tweet in tweepy.Cursor(api.search, search).items():
    tweet.retweet()
    time.sleep(600)