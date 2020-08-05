#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 3

# This bot generates one variant of a poem using a mad-libs
# technique, replacing 3 words in the original with 3
# randomly-chosen words from 3 word lists.

# Original poem: This Is Just To Say by William Carlos Williams
# https://poets.org/poem/just-say

import requests
from random import randint
from credentials import *
import tweepy, time
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# gather some corpora from GitHub using requests; these are in JSON format
animal_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/animals/common.json')
veg_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/vegetables.json')
menu_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json')

# Extract a Python-readable list from each response
animals = animal_response.json()['animals']
veg = veg_response.json()['vegetables']
menu = menu_response.json()['menuItems']
    
# Pick random numbers
# randint(0, len(xxx)-1) means choose random number between 0 and the length of the 
# word list named xxx 
animals_num = randint(0, len(animals)-1) 
veg_num = randint(0, len(veg)-1)
menu_num = randint(0, len(menu)-1)

# Choose random items from each list using those random numbers
animals_chosen = animals[animals_num].lower()
veg_chosen = veg[veg_num].lower()
menu_chosen = menu[menu_num].lower()

# Fill in the blanks of the poem with the randomly chosen items
# \n means insert a line break
# \ at end of line just splits the line in the code, so that the code can be read more easily 

poem = 'If you give a {0} a {1} they are going to ask for a {2}' \
   .format(animals_chosen, veg_chosen, menu_chosen)
for line in poem:
   print(poem)
   api.update_status(status=poem)
   time.sleep(120)



