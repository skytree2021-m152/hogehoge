'''
get_trend.py    Twitterのトレンドデータを取得する
'''

import mytw, tweepy, traceback, random,datetime

tw = mytw.MyTwitter()

if tw.api is not None:
  #リストの中から、今日、3個を検索
    for status in tw.api.search(q="list:1403224831550648321 include:nativeretweets since:{}".format(datetime.date.today()), count=3):
        
        #返ってきたtweetのidを取得
        tweet_id = status.id
        print(status) 
        # 例外処理をする
        try:
            # リツイート実行（for文の中なので繰り返す）
            tw.api.retweet(tweet_id)
        except:
            print('error')

else:
    print(traceback.format_exc())

