from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('mongodb://localhost:55017/')

db = client.test_database
collection = db.test_collection
posts = db.posts

pprint.pprint(posts.find_one({"author": "Miguel"}))

# pprint.pprint(posts.find_one({"_id": "652957d0b614b9739f614513"}))

#for post in posts.find():
#    pprint.pprint(post)

print(posts.count_documents({}))

d = datetime.datetime(2023, 10, 13, 14, 43)

for post in posts.find({"$and": [{"author": 'Miguel'}, {"date": {"$lt": d}}]}):
    print(post)
