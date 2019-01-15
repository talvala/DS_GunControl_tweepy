from pymongo import MongoClient
from collections import defaultdict


class DBUtils(object):

    def __init__(self):
        self._client = MongoClient('')
        self._db = self._client.bigdata2

    def align_country_names(self):
        """
        this method runs over the tweets and aligns location names with the countries mapping collection"
        """
        country_names_mapping = self._map_country_names()

        for tweet in self._db.tweets.find():
            location = tweet.get('location')
            if not location or location == 'None':
                continue
            for c in country_names_mapping:

                if c['name'] in location:
                    self._db.tweets.update({'_id': tweet['_id']}, {"$set": {'location': c['db_name']}})
                    print("setting location {} to {}".format(location, c['name']))
                    break

                elif c['short_name'] in location:
                    self._db.tweets.update({'_id': tweet['_id']}, {"$set": {'location': c['db_name']}})
                    print("setting location {} to {}".format(location, c['short_name']))
                    break

                else:
                    pass

    def _map_country_names(self):
        all_countries = self._db.countries_format_names.find()
        return [{
            k: v for k, v in country.items() if k != '_id'} for country in all_countries
        ]

    def process_tweets(self):
        counter = defaultdict(int)
        country_names_mapping = self._map_country_names()
        valid_location_names = [c['db_name'] for c in country_names_mapping]

        for tweet in self._db.tweets.find():
            location = tweet['location']
            if location not in valid_location_names:
                continue
            sentiment = tweet.get('sentiment')
            if not sentiment:
                continue
            if sentiment == 'negative':
                counter[location] -= 1
            elif sentiment == 'positive':
                counter[location] += 1

        for country in self._db.countries.find():
            state = country.get('state')
            state_sentiment = counter.get(state)
            if not state_sentiment:
                self._db.countries.update({'_id': country['_id']}, {"$set": {'tweet_sentiment': 'neutral'}})
                print("setting {} to be neutral".format(state))
            elif state_sentiment > 0:
                self._db.countries.update({'_id': country['_id']}, {"$set": {'tweet_sentiment': 'for'}})
                print("setting {} to be for".format(state))
            else:  # state_sentiment < 0
                self._db.countries.update({'_id': country['_id']}, {"$set": {'tweet_sentiment': 'against'}})
                print("setting {} to be against".format(state))


if __name__ == "__main__":
    db_util = DBUtils()
    db_util.process_tweets()
