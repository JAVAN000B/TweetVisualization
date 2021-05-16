import json
import datetime
import re

import emojis

with open('words', 'r') as rf:
    words = rf.readlines()
    for i in range(len(words) - 1):
        words[i] = words[i][:-1].strip()
    words = set(words)


def get_state_place(place_fullname: str, place_type: str):
    if place_type == 'city':
        place_list = place_fullname.split(', ')
        country = 'Australia'
        try:
            state = place_list[1]
            city = place_list[0]
        except:
            state = 'unknown'
            city = 'unknown'
            return city, state, country
        return city, state, country
    else:
        country = 'Australia'
        state = 'unknown'
        city = 'unkown'
        return city, state, country


def get_hashtag(hashtag_dict_list: list):
    hashtags = set()
    for hashtag_dict in hashtag_dict_list:
        hashtags.add(hashtag_dict['text'])
    return list(hashtags)


def get_zanghua(content: str):
    zanghua = []
    flag = 0
    for one_word in content.split(' '):
        if one_word in words:
            flag = 1
            zanghua.append(one_word)
    return flag, zanghua


def get_emoji(content: str):
    new_list = list(emojis.get(content))
    return new_list, 1 if len(new_list) > 0 else 0


def process_tweet(data):
    try:
        content = data['extended_tweet']['full_text']
    except:
        content = data['text']
    id = data["id_str"]
    full_date = str(datetime.datetime.strptime(
        data['created_at'], '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=datetime.timezone.utc))
    date_list = re.split('-| |:', full_date)
    year = int(date_list[0])
    mounth = int(date_list[1])
    date = int(date_list[2])
    hour = int(date_list[3])
    minute = int(date_list[4])
    place_type = data['place']['place_type']
    place = data['place']['full_name']
    coordinates = str(data['place']['bounding_box']['coordinates'])
    hashtags = data['entities']['hashtags']

    city, state, country = get_state_place(place, place_type)
    hashtags_list = get_hashtag(hashtags)
    flag_zanghua, zanghua = get_zanghua(content)
    emojis, flag_emoji = get_emoji(content)

    handle_data = {'_id': id, 'content': content, 'full_date': full_date, 'year': year, 'month': mounth, 'date': date,
                   'hour': hour, 'minute': minute, 'place': place, 'city': city, 'state': state,
                   'country': country, 'coordinates': coordinates, 'hashtags': hashtags_list,
                   'flag_vulgar': flag_zanghua, 'vulgar_word': zanghua, 'flag_emoji': flag_emoji, 'emojis': emojis}
    return handle_data

