import json
from collections import defaultdict

from flask import Flask, request

from backend import couchdbUtils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/couchdb/view/num_tweet_city/', methods=['GET', 'POST'])
def get_num_tweet_city():
    data = request_parse(request)
    city_name = data.get("city_name")
    if city_name != "all":
        json_res = couchdbUtils.get_view('&key="{}"'.format(city_name), 'tweet_latest', 'tweet_latest',
                                         'num_tweet_city', 1)
    else:
        json_res = couchdbUtils.get_view("", 'tweet_latest', 'tweet_latest', 'num_tweet_city', 1)
    return json_res


@app.route('/couchdb/view/num_tweet_state/', methods=["GET", "POST"])
def get_num_tweet_state():
    data = request_parse(request)
    state_name = data.get("state_name")
    if state_name != "all":
        json_res = couchdbUtils.get_view('&key="{}"'.format(state_name), 'tweet_latest', 'tweet_latest',
                                         'num_tweet_state', 1)
    else:
        json_res = couchdbUtils.get_view("", 'tweet_latest', 'tweet_latest', 'num_tweet_state', 1)
    return json_res


@app.route('/couchdb/view/hashtag/<place_level>/total', methods=['GET', 'POST'])
def get_hashtag_total(place_level):
    data = request_parse(request)
    if place_level == 'city':
        return get_hashtag_city_total(data)
    if place_level == 'state':
        return get_hashtag_state_total(data)
    return {404: "not found"}


def get_hashtag_city_total(data):
    # data = request_parse(request)
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'hashtag_city', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


def get_hashtag_state_total(data):
    # data = request_parse(request)
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'hashtag_state', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


@app.route('/couchdb/view/vulgar_word/<place_level>/total', methods=["GET", "POST"])
def get_vulgar_word_total(place_level):
    data = request_parse(request)
    if place_level == 'city':
        return get_vulgar_word_city_total(data)
    if place_level == 'state':
        return get_vulgar_word_state_total(data)
    return {404: "not found"}


def get_vulgar_word_city_total(data):
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'vulgar_word_city', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


def get_vulgar_word_state_total(data):
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'vulgar_word_state', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


@app.route('/couchdb/view/emojis/<place_level>/total', methods=["GET", "POST"])
def get_emojis_total(place_level):
    data = request_parse(request)
    if place_level == 'city':
        return get_emojis_city_total(data)
    if place_level == 'state':
        return get_emojis_state_total(data)
    return {404: "not found"}


def get_emojis_city_total(data):
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'emojis_city', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


def get_emojis_state_total(data):
    condition, group_level = get_condition_grouplevel(data)
    if not condition or not group_level:
        return {500: "bad request"}
    jsonRes = couchdbUtils.get_view(condition, 'tweet_latest',
                                    'tweet_latest', 'emojis_state', group_level)
    res = process_resDict(jsonRes, group_level)
    return res


# hashtag per city
@app.route('/couchdb/view/hashtag_city/<startkey>-<endkey>/<group_level>')
def get_hashtag_city(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'hashtag_city', group_level)
        return jsonRes
    else:
        # jsonRes = couchdbUtils.get_view("", 'tweet_latest', 'tweet_latest', 'hashtag_city', 1)
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'hashtag_city', group_level)
        return jsonRes


# hashtag per state
@app.route('/couchdb/view/hashtag_state/<startkey>-<endkey>/<group_level>')
def get_hashtag_state(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'hashtag_state', group_level)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'hashtag_state', group_level)
        return jsonRes


# vulgar word per city
@app.route('/couchdb/view/vulgar_word_city/<startkey>-<endkey>/<group_level>')
def get_vulgar_word_city(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'vulgar_word_city', group_level)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'vuglar_word_city', group_level)
        return jsonRes


# vulgar word per state
@app.route('/couchdb/view/vulgar_word_state/<startkey>-<endkey>/<group_level>')
def get_vulgar_word_state(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'vulgar_word_state', group_level)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'vuglar_word_state', group_level)
        return jsonRes


# emojis per city
@app.route('/couchdb/view/emojis_city/<startkey>-<endkey>/<group_level>')
def get_emojis_city(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'emojis_city', group_level)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'emojis_city', group_level)
        return jsonRes


# emojis per state
@app.route('/couchdb/view/emojis_state/<startkey>-<endkey>/<group_level>')
def get_emojis_state(startkey, endkey, group_level):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'emojis_state', group_level)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest',
                                        'tweet_latest', 'emojis_state', group_level)
        return jsonRes


# Utils Methods
def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.get_data()
        data = json.loads(data)
    elif req_data.method == 'GET':
        data = req_data.args
    return data


def get_condition_grouplevel(data):
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    place_name = data.get("place_name")
    module = data.get("module")
    place_name_start = "\"" + place_name + "\"" if place_name != "all" else "null"
    place_name_end = "\"" + place_name + "\"" if place_name != "all" else "{}"
    start_time_split = start_time.split("-")
    end_time_split = end_time.split("-")
    start_year = start_time_split[0] if start_time_split[0] != "0" else "null"
    start_month = start_time_split[1] if start_time_split[1] != "0" else "null"
    start_date = start_time_split[2] if start_time_split[2] != "0" else "null"
    end_year = end_time_split[0] if end_time_split[0] != "0" else "{}"
    end_month = end_time_split[1] if end_time_split[1] != "0" else "{}"
    end_date = end_time_split[2] if end_time_split[2] != "0" else "{}"
    if module == 'get_feature':
        group_level = 5
    else:
        if start_date != 'null':
            group_level = 4
        elif start_month != 'null':
            group_level = 3
        elif start_year != 'null':
            group_level = 2
        elif place_name:
            group_level = 1
        else:
            return None, None
    condition = "&startkey=[{},{},{},{}".format(place_name_start, start_year, start_month, start_date) \
                + ",null]" + "&endkey=[{},{},{},{}".format(place_name_end, end_year, end_month, end_date) + ",{}]"
    # print(condition)
    # print(group_level)
    return condition, group_level


def process_resDict(jsonRes, group_level):
    res_Dict = defaultdict(int)
    if group_level == 5:
        for node in jsonRes['rows']:
            hash_tag = str(node["key"][-1])
            res_Dict[hash_tag] += node["value"]
    else:
        for node in jsonRes['rows']:
            res_Dict["res"] += node["value"]
    sort_Dict = dict(sorted(res_Dict.items(), key=lambda item: item[1], reverse=True)[:15])
    return sort_Dict


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False)  # in local plz use test service
    app.run()  # test mode
