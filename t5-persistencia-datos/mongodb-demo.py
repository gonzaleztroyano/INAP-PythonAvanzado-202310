from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('mongodb://localhost:55017/')

db = client.test_database
collection = db.test_collection
posts = db.posts

for i in range(1, 50, 1):
    post = {"author": "Miguel",
            "text": "¡Mi post en el blog número {}!".format(i),
            "tags": ["mongodb", "python", "pymongo", ],
            "date": datetime.datetime.now(datetime.UTC)}

    post_id = posts.insert_one(post).inserted_id
    print(post_id)

db.list_collection_names()

pprint.pprint(posts.find_one())