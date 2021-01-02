#!/usr/bin/env python3
import tweepy 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"

class listener(StreamListener):
    def on_data(self,t):
        csvFile = open("tweets.csv" , "a")
        csvFile.write(t)
        csvFile.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
stream = Stream(auth,listener())
stream.filter(track=["xxxxxxxxx"])