from pymongo import MongoClient

import json

client = MongoClient('mongodb://db_user:dbuser123@ds157204.mlab.com:57204/bigdata2')
mydb = client.bigdata2


def add_tweet(text, location):
    mydb.tweets.insert_one(
        {
            "text": text,
            "location": location,

        })


jsonString = open("test.json", 'r')
jsonObject = json.load(jsonString)
for line in jsonObject:
    text = line['text']
    print('text:')
    print(text)
    location = line['location']
    print('location:')
    print(location)
    add_tweet(text, location)
