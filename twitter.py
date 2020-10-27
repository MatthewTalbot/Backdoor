import tweepy, time, sys
import tweepy
from tweepy import StreamListener
from tweepy import Stream
from configparser import ConfigParser
#Twitter
config = ConfigParser()
config.read('config.ini')

consumer_key = config['KEYS']['CONSUMER_KEY']
consumer_secret = config['KEYS']['CONSUMER_SECRET']
access_token = config['KEYS']['ACCESS_TOKEN']
access_secret = config['KEYS']['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):

	#Gets the message of the tweet
	def on_status(self, status):
		try:
			twitter_message = str(status.extended_tweet["full_text"])
			print(twitter_message)
		except AttributeError:
			twitter_message = str(status.text)
			print(twitter_message)

	def on_error(self, status_code):
		if status_code == 420:
			return False

