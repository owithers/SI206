import tweepy
from textblob import TextBlob
# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
access_token = "334833849-AhmmDfKqzhmrUqiBvvDxuu72zYtlisCi4SKbxbXC"
access_token_secret = "5tJcCaiyrYrisnHGcgB2UdCbIcYC6JqkzgKpVBm4LFYln"
consumer_key = "l2VJXXmanx6CpxWqXZ6bbfWBq"
consumer_secret = "J9csrcFCZDldO2407Vmgs3QYCm6SHlEB9ZGfHSIEPfDRiLMYFy"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('"Kanye" @kanyewest')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

print("Average subjectivity is") #for loop to go through the sentiments same for polarity
print("Average polarity is")
