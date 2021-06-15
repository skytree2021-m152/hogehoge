#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random
import mytw, tweepy, traceback,datetime
import requests, datetime, json, os, sys, psycopg2, traceback, configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# InsecureRequestWarning対策
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tw = mytw.MyTwitter()

#ツイートIDのリスト
idlist=[]
#ツイートのステータス(JSON)のリスト
statuses=[]
#Webサイトに埋め込む用HTMLのリスト
umekomi=[]
#umekomiをもらうためのURL
geturl = "https://api.twitter.com/1.1/statuses/oembed.json?id="

if tw.api is not None:
  #リストの中から最新3ツイートを取得(リツイートを含む)
    for status in tw.api.list_timeline(list_id=1403224831550648321, count=3, include_rts=1):
      #リツイートされたものか判定
        if "retweeted_status" in status._json:
          #print("リツイートされているツイート",status.id)

          #リツイートされた元々のツイートを引っ張ってくる処理
          tweet_id = status._json["retweeted_status"]["id"]
          idlist.append(tweet_id)
          stat = tw.api.get_status(tweet_id)
          statuses.append(stat._json)
      
        else:
          #print("リツイートではないツイート",status.id)
          #返ってきたtweetのidを取得
          tweet_id = status.id
          idlist.append(tweet_id)
          statuses.append(status._json)

else:
    print(traceback.format_exc())

#print(idlist)

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

#umekomiを確認
#print(umekomi)

for i in range(len(statuses)):

  #urlのあるツイートか判定
  if statuses[i]["entities"]["urls"]:
    print(i+1,"個目のツイートのリンクは",statuses[i]["entities"]["urls"][0]["url"])
    #ここに松井さんのスクレイピング

  else:
    print(i+1,"個目のツイートにはリンクが貼られていないので本文を取得")
    #ここに下田さんの本文取得

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'TWITTER トレンド'

print('''
Content-type: text/html

<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<title>{title}</title>

</head>

<body>

<h2>{title}</h2> 
<p>ページ説明を入れる予定</p>

{tw1}{tw2}{tw3}

<main>
    <section>
      <form action="/cgi-bin/step2.py" method="post">
      <dl>
        <dt>リスト検索</dt><dd><select id="activity" name="activity"><option value="">-----</option><option value="1">IT</option><option value="2">News</option><option value="3">スポーツ</option><option value="4">芸能・エンタメ</option></select></dd>
      </dl>
      <button class="btn">入力</button>
      </form>
    </section>
</main>

</body>
</html>
'''[1:-1].format(title=title_str,tw1=umekomi[0],tw2=umekomi[1],tw3=umekomi[2]))