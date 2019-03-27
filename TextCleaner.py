import re
from pymongo import MongoClient


DB_NAME = 'bigdata'


class TextCleaner(object):

    def __init__(self):
        self._db = self._get_db_by_name(DB_NAME)
    
    @staticmethod
    def _get_db_by_name(db_name):
        client = MongoClient('')
        return client[db_name]
    
    def clear_text(self):
        """
        this method runs on all tweets and deletes the non letters or numbers characters
        """
        for tweet in self._db.tweets.find():
            new_text = re.sub('[%]', '', tweet['text'])
            print("old text {}".format(tweet['text']))
            print("new text {}".format(new_text))
            self._db.tweets.update({'_id': tweet['_id']}, {"$set": {'text': new_text}})


if __name__ == "__main__":
    cleaner = TextCleaner()
    cleaner.clear_text()
