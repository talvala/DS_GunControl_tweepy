from pymongo import MongoClient

import json

client = MongoClient('mongodb://db_user:dbuser123@ds157204.mlab.com:57204/bigdata2')
mydb = client.bigdata2


def add_country(state,population,precentage,opinion,governor,governor_opinion):
    mydb.countries.insert_one(
            {
            "state" : state,
            "population" : population,
            "precentage" : precentage,
            "opinion" : opinion,
            "governor" : governor,
            "governor_opinion" : governor_opinion

            })

jsonString = open("countries.json", 'r')
jsonObject = json.load(jsonString)
for line in jsonObject:

    state = line['state']
    population = line['population']
    precentage = line['precentage']
    opinion = line['opinion']
    governor = line['governor']
    governor_opinion = line['governor_opinion']
    add_country(state,population,precentage,opinion,governor,governor_opinion)



