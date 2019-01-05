import tweepy
import json

# Specify the account credentials in the following variables:
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
    # Decode the JSON data
        data = json.loads(data)
        print(data)
        location = data['user']['location']

        if 'extended_tweet' in data:
            if 'full_text' in data['extended_tweet']:
                text = data['extended_tweet']['full_text']
        else:
            text = data['text']

    print_string = {{text}"{0}"{location}"{1}"}.format(text,location)
    print(print_string)
    #print (json.dumps({'text': text, 'location': location}))
    
    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()


# Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

# Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['second amendment','gun control','guns in america'])
