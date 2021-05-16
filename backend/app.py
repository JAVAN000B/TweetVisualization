from flask import Flask
from backend import couchdbUtils
import couchdb

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/couchdb/view/')
# def couchdb_get_all_city():
#     jsonRes = couchdbUtils.get_view('tweet_loc', 1)
#     return jsonRes
@app.route('/couchdb/view/num_tweet_city/<city_name>')
def get_num_tweet_city(city_name):
    if city_name != "all":
        jsonRes = couchdbUtils.get_view('&key="{}"'.format(city_name),'tweet2','tweet2','num_tweet_city',1)
        return jsonRes
    else:
        jsonRes = couchdbUtils.get_view("",'tweet2','tweet2','num_tweet_city',1)
        return jsonRes

# @app.route('/couchdb/view/num_tweet_state')
# def get_num_tweet_state():
#     jsonRes = couchdbUtils.get_view('tweet2','tweet2','num_tweet_state',1)
#     return jsonRes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)  # in local plz use test service
    # app.run() # test mode
