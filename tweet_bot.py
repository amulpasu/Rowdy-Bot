import tweepy
import time
from apscheduler.schedulers.blocking import BlockingScheduler

from os import environ
consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token = environ['TWITTER_ACCESS_TOKEN_KEY']
access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search = 'list:Rowdy_Bot/dvs include:nativeretweets'


def dvs_list():
    for tweet in tweepy.Cursor(api.search, search, result_type="recent").items(4):
        try:
            tweet.retweet()
            time.sleep(600)
        except tweepy.TweepError:
            time.sleep(600)
            continue
        except StopIteration:
            break


scheduler = BlockingScheduler()
scheduler.add_job(dvs_list, 'interval', hours=1)
scheduler.start()
