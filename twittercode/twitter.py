import tweepy

# Unique code from Twitter
access_token = "334833849-AhmmDfKqzhmrUqiBvvDxuu72zYtlisCi4SKbxbXC"
access_token_secret = "5tJcCaiyrYrisnHGcgB2UdCbIcYC6JqkzgKpVBm4LFYln"
consumer_key = "l2VJXXmanx6CpxWqXZ6bbfWBq"
consumer_secret = "J9csrcFCZDldO2407Vmgs3QYCm6SHlEB9ZGfHSIEPfDRiLMYFy"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

