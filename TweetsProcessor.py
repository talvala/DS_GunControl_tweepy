from pymongo import MongoClient
from collections import defaultdict

DB_NAME = 'bigdata2'


class TweetsProcessor(object):

    def __init__(self):
        self._db = self._get_db_by_name(DB_NAME)
    
    @staticmethod
    def _get_db_by_name(db_name):
        client = MongoClient('')
        return client[db_name]

    def _map_country_names(self):
        all_countries = self._db.countries_format_names.find()
        return [{
            k: v for k, v in country.items() if k != '_id'} for country in all_countries
        ]

    def process_tweets(self):
        state2sentiment_counter = defaultdict(int)
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
                state2sentiment_counter[location] -= 1
            elif sentiment == 'positive':
                state2sentiment_counter[location] += 1
        self._update_tweets_sentiment(state2sentiment_counter)
        
    def _update_tweets_sentiment(self, mapper):
        for country in self._db.countries.find():
            state = country.get('state')
            state_sentiment = mapper.get(state)
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
    processor = TweetsProcessor()
    processor.process_tweets()
