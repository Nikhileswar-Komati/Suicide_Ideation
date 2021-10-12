import tweepy
import time
import pandas as pd

# api key
api_key = "YfsfRUtv0Jstlvm0TLg8DrZNA"
# api secret key
api_secret_key = "Dx95SabGPVACrlQanwkajOnsfss0tWsyej8xO8rUKnf6N70Tyh"
# access token
access_token = "704330902432669696-pmTtYoAM3ywia3zAY5sWAEVkzhWUwan"
# access token secret
access_token_secret = "BSW1LmSmDZmNrDPL3KytWXgZeOTHo99Ee1vDu1FBc5EAJ"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 100
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count, lang = 'en'):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
