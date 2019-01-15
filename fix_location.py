from pymongo import MongoClient


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
        return [{k: v for k, v in country.items() if k != '_id'} for country in all_countries]


if __name__ == "__main__":
    db_util = DBUtils()
    db_util.align_country_names()
