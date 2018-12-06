from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from twitter_credentials import CONSUMER_KEY,CONSUMER_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

class StdOutListener(StreamListener):
	def on_data(self, data):
		print(data)
		return True

	def on_error(self, status):
		print(status)

if __name__ == "__main__":
	listener = StdOutListener()
	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	
	stream = Stream(auth, listener)
	
	stream.filter(track=['second amendment','gun control','guns in america'])

	
