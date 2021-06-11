'''
mytw.py twitter APIに接続するプログラムのためのクラス定義
'''

import tweepy, os, sys, json, configparser, traceback

# 定数（ファイル名など）
CONF_FILE   = 'tw.ini'

class MyTwitter:

    api = None
    
    def __init__(self, twitter_id='SKYTREE2021_01'):

        config = configparser.ConfigParser()

        if os.path.exists(CONF_FILE):
            
            config.read(CONF_FILE)
            tw = config[twitter_id]

            consumer_key        = tw['API_KEY']
            consumer_secret     = tw['API_SECRET_KEY']
            access_token        = tw['ACCESS_TOKEN']
            access_token_secret = tw['ACCESS_TOKEN_SECRET']
            
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
           
            try:
                self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            except:
                print(traceback.format_exc())
                sys.exit(1)

        else:
            print(traceback.format_exc())
            self.api = None
            sys.exit(1)

