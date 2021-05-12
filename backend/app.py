from flask import Flask
import couchdbUtils
import couchdb

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/couchdb/view/')
def couchdb_get_all_city():
    jsonRes = couchdbUtils.get_view('tweet_loc', 1)
    return jsonRes


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)  # in local plz use test service
    # app.run() # test mode
