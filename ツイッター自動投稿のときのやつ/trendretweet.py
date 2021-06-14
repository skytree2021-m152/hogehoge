'''
get_trend.py    Twitterのトレンドデータを取得する
'''

import mytw, tweepy, traceback, random,datetime

tw = mytw.MyTwitter()

if tw.api is not None:

    woeid = {
        "日本": 23424856,
    }

    for area, wid in woeid.items():
        trends = tw.api.trends_place(wid)[0]
    
    #トレンド何位を取得するか
    rank= 2

    #トレンドのデータからn位の言葉だけ取得
    word = trends["trends"][rank-1]['name']
    text = "現在日本のトレンド{}位は「{}」です。".format(rank,word)
    #print(text)
    #ツイート実行
    tw.api.update_status(text)

    #トレンドn位の言葉、リツイート1000以上、今日、5個を検索
    for status in tw.api.search(q="{} min_retweets:1000 since:{}".format(word, datetime.date.today()), count=5):
        
        #返ってきたtweetのidを取得
        tweet_id = status.id

        # 例外処理をする
        try:
            # リツイート実行（for文の中なので繰り返す）
            tw.api.retweet(tweet_id)
        except:
            print('error')

else:
    print(traceback.format_exc())

