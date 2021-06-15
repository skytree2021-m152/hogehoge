#ツイートIDからstatus(JSON)を持ってくるプログラム

import mytw, tweepy, traceback,datetime
tw = mytw.MyTwitter()

#欲しいツイートのIDをここに入れる
id_ = "1404559336010092546"

if tw.api is not None:
    statuses= tw.api.get_status(id_,tweet_mode='extended')
    #print(status._json["entities"]["urls"][0]["url"])--エラーでる
    #返ってきたtweetのidを取得
    print(statuses.full_text)

else:
    print(traceback.format_exc())
