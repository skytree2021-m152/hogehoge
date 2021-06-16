import mytw, tweepy, traceback, random,datetime

tw = mytw.MyTwitter()
idlist=[]

if tw.api is not None:
  #リストの中から最新2ツイートを取得
    for status in tw.api.list_timeline(list_id=1403224831550648321, count=2):
        
        #返ってきたtweetのidを取得
        tweet_id = status.id
        idlist.append(tweet_id)


else:
    print(traceback.format_exc())

print(idlist)

