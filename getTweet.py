import sys
import tweepy
import csv
import jsonpickle
import pandas as pd
import datetime
from jsonpickle import json



# Consumer
consumer_key = "MF9HGJHix7aH40oel8O9zbc7k"
consumer_secret = "Rd97ibI3rtXTAeyQOqpnVhIWNnCJknRF5wifLw7aoFDY9O586a"

# Access
access_token ="1222006003-KZffuFWbvIZvMFYuNQDGvAQyqdo3UmPVue2bmmQ"
access_token_secret = "97GvmsPUzASgkLDEAhzhIf6nholUc3JpiYEUre8nXjj4t"

# API setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

query = "#kecelakaan"
collection = query[0]
start_date = "2019-03-01"
end_date   = "2019-03-07"



# getTweet(query,collection,start_date,end_date,query)


# Open/Create a file to append data
csvFile = open('kecelakaan01.json', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)



for tweet in tweepy.Cursor(api.search,q=query,count=9999,
                           lang="in",
                           since=start_date,
                           tweet_mode='extended').items():
    print (tweet.created_at, tweepy.User, tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.id, tweet.user.name, tweet.text])





print("Selesai")


