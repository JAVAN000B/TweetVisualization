import datetime
import json
import time
import re

import couchdb
import preprocessor as pp
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

if "tweet2" in couch:
    db = couch["tweet2"]
else:
    db = couch.create("tweet2")

with open('words', 'r') as rf:
    words = rf.readlines()
    for i in range(len(words) - 1):
        words[i] = words[i][:-1].strip()
    words = set(words)


def get_state_place(place_fullname: str):
    place_list = place_fullname.split(', ')
    return place_list[0], place_list[1]


def get_hashtag(hashtag_dict_list: list):
    hashtags = []
    for hashtag_dict in hashtag_dict_list:
        hashtag_list = list(hashtag_dict.keys())
        for hashtag in hashtag_list:
            hashtags.append(hashtag)
    return hashtags


def get_zanghua(content: str):
    zanghua = []
    flag = 0
    for one_word in content.split(' '):
        if one_word in words:
            flag = 1
            zanghua.append(one_word)
    return flag, zanghua


def get_emoji(content: str):
    temp1 = pp.clean(content)
    temp2 = re.sub('[a-zA-Z]', '', temp1)
    emojis = temp2.split()
    return emojis, 1 if len(emojis) > 0 else 0


class StdOutListener(StreamListener):
    def __init__(self):
        pass

    def on_data(self, data):
        print(data)
        data = json.loads(data)
        content = data['text']
        # date = data['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        id = data["id_str"]
        date = str(datetime.datetime.strptime(
            data['created_at'], '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=datetime.timezone.utc))
        place = data['place']['full_name']
        coordinates = str(data['place']['bounding_box']['coordinates'])
        hashtags = data['entities']['hashtags']

        city, state = get_state_place(place)
        hashtags_list = get_hashtag(hashtags)
        flag_zanghua, zanghua = get_zanghua(content)
        emojis, flag_emoji = get_emoji(content)
        # flag = 0
        # zanghua = []
        # for one_word in content.split(' '):
        #     if one_word in words:
        #         flag = 1
        #         zanghua.append(one_word)

        handle_data = {'_id': id, 'content': content, 'date': date, 'place': place, 'city': city, 'state': state,
                       'coordinates': coordinates, 'hashtags': hashtags_list, 'flag_zanghua': flag_zanghua,
                       'zanghua': zanghua, 'flag_emoji': flag_emoji, 'emojis': emojis}
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
    consumer_key = "Sfpku4OPfTmG6zHqjZurroJH7"  # write consumer key here
    # write consumer secret here
    consumer_secret = "DWrBRxYuFYGqeh5Vy7HZdkRL4WFskeTCaxvlzYjbvfgv1EFvDL"
    # write access_token here
    access_token = "1385175482149208068-BBDqWpVlIzwB6njWAKCebzkqkOakbX"
    # write access token secret here
    access_token_secret = "uX7uaR9vjIzO6CtXixf4ZqXoFmnqHoTFN3Eg1mbSNQ1pQ"

    # Search Area: Australia
    # locations = city_locations['Darwin']

    # Keywords for Search in Twitter: A list of strings
    # keywords=['study','education','homeschooling','school','homework','assignment']

    twitter_streamer = TwitterStreamer("AU")

    # (Server, Database Name, Keywords)
    twitter_streamer.stream_tweets()
