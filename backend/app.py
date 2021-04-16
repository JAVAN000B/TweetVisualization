from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getTweet/')
def get_tweet():
    return None


if __name__ == '__main__':
    app.run()
