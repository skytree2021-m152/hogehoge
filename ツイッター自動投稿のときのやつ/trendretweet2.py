'''
get_trend.py    Twitterのトレンドデータを取得する
'''

import mytw, tweepy, traceback, random,datetime

tw = mytw.MyTwitter()

if tw.api is not None:
  #リストの中から、今日、3個を検索
    for status in tw.api.list_timeline(list_id=1403224831550648321, count=2):
        
        #返ってきたtweetのidを取得
        tweet_id = status.id
        print(tweet_id)
        # 例外処理をする
        try:
            # リツイート実行（for文の中なので繰り返す）
            tw.api.retweet(tweet_id)
        except:
            print('error')

else:
    print(traceback.format_exc())

