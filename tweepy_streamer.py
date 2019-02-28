import tweepy
import json

# Specify the account credentials in the following variables:
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):

    def on_data(self, data):
        # Decode the JSON data
        data = json.loads(data)
        if not data['text'].startswith('RT'):
            location = data['user']['location']

            if 'extended_tweet' in data:
                if 'full_text' in data['extended_tweet']:
                    text = data['extended_tweet']['full_text']
            else:
                text = data['text']

            items = {"text": text, "location": location}
            out = json.dumps(items)
            print(out)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()
    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener, timeout=18000)
    stream.filter(
        track=['second amendment', 'gun control', 'guns in america', '2nd amendment', 'guns control', 'america guns',
               'america shooting', 'shooting america', 'control guns', 'guns america', 'usa guns', 'guns usa', 'usa shooting', 'guns in usa','amendment second','amendment 2nd','2 amendment','amendment 2', 'control guns','shooring usa','shooring america','america shooting'])
