import sys
import json
import tweepy
##from pymongo import MongoClient
##
##client = MongoClient()
##db = client.twitter_db
##twitter_collection = db.tweets

ckey = "IFaR1G0rY9eDlozCW9rQLMYm8"
csecret = "sSRLMSmznbAxG84aVZISi9hw10tyi5C7huRXZhD9v0qSuWwsG1"
atoken = "125676011-4tojNw0MbZyvQAW4oEBeNSHp4K1jt0VBJKeFkkRG"
asecret = "DVyogW3GMw5boI6dE05vpE2l6gN5miyx5WMctYGNRDg5a"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

tweets = []
#save_file = open('20thMay.json', 'a')


class MyStreamListener(tweepy.StreamListener):

    """def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.save_file = tweets"""

##    def on_status(self, status):
##        try:
##            twitter_json = status._json
##            
##            tweet_id = twitter_collection.insert(twitter_json)
##            print(json.dumps(status.text))
##        except:
##            pass
    def on_status(self, status):
        print(json.dumps(status.text))

    """def on_data(self, tweet):
        self.save_file.append(json.loads(tweet))
        print(tweet)
        save_file.write(str(tweet))"""
    
    def on_error(self, status_code):
        print(sys.stderr, 'Encounterd error', status_code)
        return TrueS

    def on_timeout(self):
        print(sys.stderr, 'Timeout')
        return True

#MyStreamListener = MyStreamListener()
sapi = tweepy.streaming.Stream(auth = api.auth, listener = MyStreamListener())
sapi.filter(track = ['Brexit'])

