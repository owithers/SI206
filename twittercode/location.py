import tweepy
from textblob import TextBlob

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

public_tweets = api.search('"Gilmore Girls" geocode:40.6781784,-73.94415789999999,10km')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
