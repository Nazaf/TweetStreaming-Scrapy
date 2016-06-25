import sys
import json
import tweepy

ckey = ""
csecret = ""
atoken = ""
asecret = ""

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

tweets = []

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(json.dumps(status.text))
    
    def on_error(self, status_code):
        print(sys.stderr, 'Encounterd error', status_code)
        return TrueS

    def on_timeout(self):
        print(sys.stderr, 'Timeout')
        return True

#MyStreamListener = MyStreamListener()
sapi = tweepy.streaming.Stream(auth = api.auth, listener = MyStreamListener())
sapi.filter(track = ['Brexit'])

