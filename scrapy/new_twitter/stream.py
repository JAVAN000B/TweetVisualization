import datetime
import json
import time

import processing

import couchdb
import emojis
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

city_locations = {
    'Melbourne': [144.668792, -38.312755, 145.378509, -37.705070],
    'Tasmania': [147.175928, -43.082853, 147.674799, -42.598515],
    'Sydney': [150.902511, -34.007028, 151.316184, -33.644015],
    'Darwin': [130.825607, -12.467706, 130.935127, -12.371143],
    'AU': [113.328104, -42.831753, 156.921851, -13.095645]
}

# city = 'Melbourne'

couch = couchdb.Server("http://admin:admin@172.26.134.75:5984")

if "tweet_latest" in couch:
    db = couch["tweet_latest"]
else:
    db = couch.create("tweet_latest")

with open('words', 'r') as rf:
    words = rf.readlines()
    for i in range(len(words) - 1):
        words[i] = words[i][:-1].strip()
    words = set(words)


class StdOutListener(StreamListener):
    def __init__(self):
        pass

    def on_data(self, data):
        print(data)
        data = json.loads(data)
        handle_data = processing.process_tweet(data)
        db.save(handle_data)
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            time.sleep(10)
            # return False
        if status == 429:
            print("limit again? why not use twint **sign**")
            time.sleep(1200)
        else:
            print("unexpected error. I dont know about this but sorry")
            time.sleep(10)


class TwitterStreamer:
    def __init__(self, city):
        self.city = city

    def stream_tweets(self):
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        stream.filter(locations=city_locations[f'{self.city}'], languages=['en'])


#####################################################################################


#####################################################################################
if __name__ == "__main__":
    # Twitter API Credentials
    consumer_key = "kUx4tq1D61dsPoTiJ9mO5A3OR"  # write consumer key here
    # write consumer secret here
    consumer_secret = "qHN1ckce9d9Oc197S5vOnkjCmIuUiCcbtYcbemiQsBMVwOV1bn"
    # write access_token here
    access_token = "1385175482149208068-XZk18dDjLWJHnmetkssILlcGCsNhP9"
    # write access token secret here
    access_token_secret = "bIR7kU56QLNoPWHDOy03GCijv6BdvQgwrN2jXAz8CtIJO"

    twitter_streamer = TwitterStreamer("AU")

    twitter_streamer.stream_tweets()
