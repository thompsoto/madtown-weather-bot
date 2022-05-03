import tweepy
import weather
import os

all_keys = open(os.path.abspath('tweepykeys.txt'), 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]
bearer_token = all_keys[4]

client = tweepy.Client(
    bearer_token, api_key, api_key_secret, access_token, access_token_secret
)

if weather.curr_time < 12:
    client.create_tweet(text=weather.morning_msg)
else:
    client.create_tweet(text=weather.night_msg)