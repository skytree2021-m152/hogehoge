#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random
import mytw, tweepy, traceback,datetime
import requests, datetime, json, os, sys, psycopg2, traceback, configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# InsecureRequestWarning対策
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


tw = mytw.MyTwitter()
idlist=[]
statuses=[]
umekomi=[]
geturl = "https://api.twitter.com/1.1/statuses/oembed.json?id="

if tw.api is not None:
  #リストの中から最新3ツイートを取得(リツイートを含む)
    for status in tw.api.list_timeline(list_id=1403234425500884994, count=3, include_rts=1):
        #print(status._json["entities"]["urls"][0]["url"])--エラーでる
        #返ってきたtweetのidを取得
        tweet_id = status.id
        idlist.append(tweet_id)
        statuses.append(status._json)

else:
  print(traceback.format_exc())

print(statuses[2])

print(idlist)

#GetJMADataの定義、JSONとってくる
def GetJMAData(request):
    try:
        res = requests.get(request,verify=False)
        return res.json()
    except Exception:
        return None

if __name__ == '__main__':
  #idlistの長さだけfor文(3回予定)
  for i in range(len(idlist)):
    #リクエストURLにツイートIDつける
    request = geturl+str(idlist[i])
    res = GetJMAData(request)
    #JSONデータ(res)のhtmlをumekomiリストに入れる
    umekomi.append(res["html"])

#umekomiを確認(いらなくなったら#つけてください)
#print(umekomi)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'TWITTER トレンド'