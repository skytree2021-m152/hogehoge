def gettweets(list_id_=1404673140899282948):
    idlist=[]

    #リストの中から最新3ツイートを取得(リツイートを含む)
    for status in tw.api.list_timeline(list_id=list_id_, count=3, include_rts=1):
        #リツイートされたものか判定
        if "retweeted_status" in status._json:
            #print("リツイートされているツイート",status.id)

        #リツイートされた元々のツイートを引っ張ってくる処理
            tweet_id = status._json["retweeted_status"]["id"]
            idlist.append(tweet_id)
        
        else:
            #print("リツイートではないツイート",status.id)
            #返ってきたtweetのidを取得
            tweet_id = status.id
            idlist.append(tweet_id)

    return idlist