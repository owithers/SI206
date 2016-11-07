import tweepy
import json

# Unique code from Twitter
access_token = "334833849-AhmmDfKqzhmrUqiBvvDxuu72zYtlisCi4SKbxbXC"
access_token_secret = "5tJcCaiyrYrisnHGcgB2UdCbIcYC6JqkzgKpVBm4LFYln"
consumer_key = "l2VJXXmanx6CpxWqXZ6bbfWBq"
consumer_secret = "J9csrcFCZDldO2407Vmgs3QYCm6SHlEB9ZGfHSIEPfDRiLMYFy"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


