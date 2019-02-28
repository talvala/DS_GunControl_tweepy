import re

from pymongo import MongoClient


class DBUtils(object):

    def __init__(self):
        self._client = MongoClient('')
        self._db = self._client.bigdata

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
    db_util = DBUtils()
    db_util.clear_text()