from pymongo import MongoClient

import json

client = MongoClient('mongodb://.../bigdata')
mydb = client.bigdata


def add_tweet(text, location):
    mydb.tweets.insert_one(
            {
            "text" : text,
            "location" : location,

            })

jsonString = open("filteredJson.json", 'r')
jsonObject = json.load(jsonString)
for line in jsonObject:
    text = line['text']
    print('text:')
    print(text)
    location = line['location']
    print('location:')
    print(location)
    add_tweet(text, location)



