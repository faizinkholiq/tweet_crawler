import tweepy
import csv

from dotenv import load_dotenv
load_dotenv()

import os

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('dump/oleoutfortheglory.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets, q="#oleout",lang="id").items(100):
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])