#!/usr/bin/env/python 

import praw

import datetime as dt

# After creating the reddit developer account, we will receive some values, which we havr to place here.
reddit = praw.Reddit(client_id='xxxxxxxxxxxxxxx', \
                     client_secret='xxxxxxxxxxxxxxxx ', \
                     user_agent='xxxxxxxxxxx', \
                     username='xxxxxxxxxxxxxxx', \
                     password='xxxxxxxxxxxxxxxxxxx')


# Here, we will place the topic name that we have to search over the twitter
subreddit = reddit.subreddit('xxxxxxxxxxxx')

## .top() is one of the search option, we have other options like .hot(),.new(),.controversial(),.top() and .gilded()
top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=500)

## Using this we will be ale to see the data that has been scrapped using Reddit