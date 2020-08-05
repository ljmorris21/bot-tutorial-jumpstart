#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 2

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Try this with another .txt file!
# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in a plain text editor, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('lesmis.txt','r') 
tweet_text = filename.readlines() 
filename.close()

# loop through the tweet_list
for line in tweet_text[0:73345]: 
    if len(line) > 0:
        if " sewer " in line:
            try:
                print('About to tweet:')
                print(line)
                api.update_status(status=line)
                print('Tweeted.\n...')
            except:
                print("Duplicate")
            time.sleep(30)
    else:
        pass 
   
print("All done!")

# To quit early: CTRL+C and wait a few seconds