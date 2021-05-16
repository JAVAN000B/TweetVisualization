import couchdb
from backend import couchdbUtils

map_reduce_view_tweet2={
  "_id": "_design/tweet2",
  "_rev": "35-262a20938bca7a73487f4aa53a61b64c",
  "views": {
    "num_tweet_city": {
      "reduce": "_count",
      "map": "function (doc) {\n  emit(doc.city, 1);\n}"
    },
    "num_tweet_state": {
      "reduce": "_count",
      "map": "function (doc) {\n  emit(doc.state, 1);\n}"
    },
    "hashtag_city": {
      "map": "function (doc) {\n  if (doc.hashtags != 0){\n      for (var i in doc.hashtags){\n        emit([doc.city,doc.hashtags[i]],1);\n      }\n    }\n}",
      "reduce": "_count"
    },
    "num_hashtag_city": {
      "map": "function (doc) {\n  emit(doc.city, doc.hashtags.length);\n}",
      "reduce": "_sum"
    }
  },
  "language": "javascript"
}

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
