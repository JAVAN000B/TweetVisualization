import couchdb
import requests
import json

DB_USER = 'admin'
DB_PASWD = 'admin'
DB_PORT = 5984
DB_CLUSTER = ['172.26.134.75', '172.26.130.123', '172.26.129.68']
# DB_NAME = "tweet2"
URL = 'http://{username}:{password}@{host}:{port}'
URL_VIEW = '/{database}/_design/{design_doc}/_view/{view_name}?group_level={group_level}'
global count
count = 0


def connect_to():
    global count
    count += 1
    if count > 2:
        count = 0
    print('Connect to: {}'.format(DB_CLUSTER[count]))
    return DB_CLUSTER[count]


# http://admin:admin@172.26.130.123:5984/tweet2/_design/tweet2/_view/hashtag_city
def get_view(condition, db_name, designDoc_name, view_name, group_level):
    url = (URL + URL_VIEW + condition).format(username=DB_USER,
                                              password=DB_PASWD,
                                              host=connect_to(),
                                              # '172.26.130.123',
                                              port=DB_PORT,
                                              database=db_name,
                                              design_doc=designDoc_name,
                                              view_name=view_name,
                                              group_level=group_level
                                              )
    rawRes = requests.get(url).content
    jsonRes = json.loads(rawRes)
    return jsonRes


def initial_couchdb(db_name):
    # 'http://admin:admin@172.26.130.123:5984'
    couch = couchdb.Server(URL.format(DB_USER,
                                      DB_PASWD,
                                      '172.26.134.75',  # master node
                                      DB_PORT))
    if db_name in couch:
        db = couch[db_name]
    else:
        db = couch.create(db_name)

    return db
