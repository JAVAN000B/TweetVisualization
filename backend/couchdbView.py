import couchdb
from backend import couchdbUtils

def creat_view(db):
    map_reduce_view_count = {
        "_id": "_design/test",
        "views": {
            "tweet_loc": {
                "reduce": "_sum",
                "map": "function (doc) {\n  emit(doc.location, 1);\n}"
            },
            "test-view": {
                "map": "function (doc) {\n  emit(doc._id, 2);\n}"
            }
        },
        "language": "javascript"
    }
    db.save(map_reduce_view_count)

db = couchdbUtils.initial_couchdb()
creat_view(db)