import tweepy
from textblob import TextBlob

consumer_key = 'FB7pdezh3Ta9kLrzuVy3IsJgR'
consumer_secret = 'Qa988RzLtrB2Q0PuEMP9N564OI4FXg3HYs89uM4GybMrSZOApM'

acess_token = '416899445-FEtdMFUywA5xHUHm6nkc94fMvTfSHqpni91HXnPb'
access_token_secret = 'OCSQ1fa9Gjwn7oSphgag8DeNA7i1W4WeYhqK6LzED7y5S'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Donald Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
