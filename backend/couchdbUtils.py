import couchdb
import requests
import json

DB_USER = 'admin'
DB_PASWD = 'admin'
DB_PORT = 5984
DB_CLUSTER = ['172.26.134.75', '172.26.130.123', '172.26.129.68']
DB_NAME = "test1"
URL = 'http://{}:{}@{}:{}'
URL_VIEW = '/{}/_design/tweet/_view/{}?group_level={}'
global count
count = 0


def connect_to():
    global count
    count +=1
    if count >2:
        count = 0
    print('Connect to: {}'.format(DB_CLUSTER[count]))
    return DB_CLUSTER[count]


def get_view(view_name, group_level):
    url = (URL + URL_VIEW).format(DB_USER,
                                  DB_PASWD,
                                  connect_to(),
                                  DB_PORT,
                                  DB_NAME,
                                  view_name,
                                  group_level)
    rawRes = requests.get(url).content
    jsonRes = json.loads(rawRes)
    return jsonRes


def initial_couchdb():
    # 'http://admin:admin@172.26.130.123:5984'
    couch = couchdb.Server(URL.format(DB_USER,
                                      DB_PASWD,
                                      '172.26.134.75',
                                      DB_PORT))
    if DB_NAME in couch:
        db = couch[DB_NAME]
    else:
        db = couch.create(DB_NAME)

    return db
