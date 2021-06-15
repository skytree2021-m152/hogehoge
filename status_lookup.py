#ツイートIDからstatus(JSON)を持ってくるプログラム

import mytw, tweepy, traceback,datetime
tw = mytw.MyTwitter()

#欲しいツイートのIDをここに入れる
id_ = "1404559336010092546"

if tw.api is not None:
    #print(status._json["entities"]["urls"][0]["url"])--エラーでる
    #返ってきたtweetのidを取得

    #tweet_mode='extended'を入れるとfull_textが取得できるようになる
    statuses= tw.api.get_status(id_,tweet_mode='extended')
    print(statuses.full_text)

else:
    print(traceback.format_exc())
