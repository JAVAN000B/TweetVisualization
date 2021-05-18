import json

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


# bug
@app.route('/couchdb/view/hashtag_city/<startkey>/<endkey>')
def get_hashtag_city(startkey, endkey):
    if startkey and endkey:
        jsonRes = couchdbUtils.get_view('&startkey={}&endkey={}'.format(startkey, endkey), 'tweet_latest',
                                        'tweet_latest', 'hashtag_city', 5)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("", 'tweet_latest', 'tweet_latest', 'hashtag_city', 1)
        return jsonRes


# Utils Methods
def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.get_data()
        data = json.loads(data)
    elif req_data.method == 'GET':
        data = req_data.args
    return data


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False)  # in local plz use test service
    app.run()  # test mode
