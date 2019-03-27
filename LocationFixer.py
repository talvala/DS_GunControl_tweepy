import re
from pymongo import MongoClient

DB_NAME = 'bigdata'


class LocationFixer(object):

    def __init__(self):
        self._db = self._get_db_by_name(DB_NAME)
    
    @staticmethod
    def _get_db_by_name(db_name):
        client = MongoClient('')
        return client[db_name]
    
    def align_country_names(self):
        """
        this method runs over the tweets and aligns location names with the countries mapping collection"
        """
        country_names_mapping = self._map_country_names()

        self._clear_empty_location()

        tweets_to_delete = list()

        for tweet in self._db.tweets.find():
            location_update = False
            location = tweet.get('location')
            parsed_location = self._get_parsed_location(location)

            for c in country_names_mapping:

                if c['name'] in parsed_location:
                    self._db.tweets.update({'_id': tweet['_id']}, {"$set": {'location': c['db_name']}})
                    location_update = True
                    print("setting location {} to {}".format(location, c['name']))
                    break

                elif c['short_name'] in parsed_location:
                    self._db.tweets.update({'_id': tweet['_id']}, {"$set": {'location': c['db_name']}})
                    location_update = True
                    print("setting location {} to {}".format(location, c['short_name']))
                    break

                else:
                    pass
            if not location_update:
                tweets_to_delete.append(tweet['_id'])

        deleted = self._db.tweets.delete_many({'_id': {'$in': tweets_to_delete}}).deleted_count
        print("deleted {} documents with irrelevant location".format(deleted))

    @staticmethod
    def _get_parsed_location(location: str):
        split_by_capital = re.findall('[A-Z][^A-Z]*', location)
        trimmed = [word.strip() for word in split_by_capital]
        return " ".join(trimmed)

    def _clear_empty_location(self):
        deleted = self._db.tweets.delete_many(
            {'$or': [
                {'location': {'$in': [None, 'null']}},
                {'location': {'$exists': False}}
            ]}
        ).deleted_count
        print("deleted {} documents for empty location".format(deleted))

    def _map_country_names(self):
        all_countries = self._db.countries_format_names.find()
        return [{k: v for k, v in country.items() if k != '_id'} for country in all_countries]


if __name__ == "__main__":
    fixer = LocationFixer()
    fixer.align_country_names()
