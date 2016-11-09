import tweepy
from textblob import TextBlob
# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('"Yeezy" @kanyewest')

#lists to pull out each number, then do the average
subjectivity=[]
polarity=[]
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	subjectivity.append(analysis.sentiment.subjectivity)
	polarity.append(analysis.sentiment.polarity)
	print(analysis.sentiment)
av_sub= sum(subjectivity)/len(subjectivity)
av_pol= sum(polarity)/len(polarity)

print("Average subjectivity is " + str(av_sub)) 
print("Average polarity is " + str(av_pol)) 
