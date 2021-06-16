#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random
import mytw, tweepy, traceback,datetime
import requests, datetime, json, os, sys, psycopg2, traceback, configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#pythonファイルのインポート
#scraping.の後はリストに応じたファイル名を指定！
import scraping.IT_list as s,kanjou

# InsecureRequestWarning対策
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tw = mytw.MyTwitter()

#ツイートIDのリスト
idlist=[]
#ツイートのステータス(JSON)のリスト
statuses=[]
#Webサイトに埋め込む用HTMLのリスト
umekomi=[]
#感情分析に入れたい文のリスト
texts=[]
#umekomiをもらうためのURL
geturl = "https://api.twitter.com/1.1/statuses/oembed.json?id="

if tw.api is not None:
  #リストの中から最新3ツイートを取得(リツイートを含む)
    for status in tw.api.list_timeline(list_id=1403234243115819015, count=3, include_rts=1):
      #リツイートされたものか判定
        if "retweeted_status" in status._json:
          #print("リツイートされているツイート",status.id)

          #リツイートされた元々のツイートIDを引っ張ってくる処理
          tweet_id = status._json["retweeted_status"]["id"]
          idlist.append(tweet_id)
      
        else:
          #print("リツイートではないツイート",status.id)
          #返ってきたtweetのidを取得
          tweet_id = status.id
          idlist.append(tweet_id)

    for i in range(len(idlist)):
      #statusではツイート本文が途中で切れてしまう問題を解決
      stat=tw.api.get_status(idlist[i],tweet_mode='extended')
      statuses.append(stat._json)
      

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
    #ツイートに載っているリンクURLを変数に代入
    url=statuses[i]["entities"]["urls"][0]["url"]
    #urlを別ファイルに渡して実行
    text = s.func(url)
    #print(text)
    texts.append(text)

  else:
    #ツイートの本文取得
    #print(statuses[i]["full_text"])
    texts.append(statuses[i]["full_text"])

mag=[]
score=[]
#３つのツイートを感情分析APIに入れる
for i in range(3):
  res = kanjou.main(texts[i])
  #CGIの時は↓はけすこと 
  mag.append(res['documentSentiment']["magnitude"])
  score.append(res['documentSentiment']['score'])

#print(mag)
#print(score)
title_str = 'TWITTER トレンド [IT]'

print('''
Content-type: text/html

<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">


<link rel="stylesheet" href="../index2.css">
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<title>{title}</title>

</head>

<body>

<center><h1>{title}</h1></center>
<p><center>本日のニュースを気軽に読む</center></p>

<div class="flex">
<div>{tw1}</div>
<div class="balloon5">
<div class="faceicon">
<img src="https://1.bp.blogspot.com/-Zg12XWQzTQA/U7O64KmAGhI/AAAAAAAAiUY/PvNni1PWTyk/s800/whiteman2_idea.png"  width="280" height="186" />
</div>
<div class="chatting">
<div class="says">
<h2>感情のデカさ：{mag1}<br>いい話度：{sc1}</h2></div>
</div>
</div>
</div>

<div class="flex">
<div>{tw2}</div>
<div class="balloon5">
<div class="faceicon">
<img src="https://2.bp.blogspot.com/-jb-vJs48VBs/U7O64nt6_SI/AAAAAAAAiUg/N46UerPXEJU/s800/whiteman2_shock.png"  width="280" height="186" />
</div>
<div class="chatting">
<div class="says">
<h2>感情のデカさ：{mag2}<br>いい話度：{sc2}</h2></div>
</div>
</div>
</div>

<div class="flex">
<div>{tw3}</div>
<div class="balloon5">
<div class="faceicon">
<img src="https://2.bp.blogspot.com/-Bb6rSSRE9u4/U7O648vJ9oI/AAAAAAAAiUk/DpmLgnnSOZU/s800/whiteman2_surprise.png"  width="280" height="186" />
</div>
<div class="chatting">
<div class="says">
<h2>感情のデカさ：{mag3}<br>いい話度：{sc3}</h2></div>
</div>
</div>
</div>



<main>
    <button type=“button” onclick="location.href='index.py'">戻る</button>
</main>

</body>
</html>
'''[1:-1].format(title=title_str,tw1=umekomi[0],tw2=umekomi[1],tw3=umekomi[2],mag1=mag[0],mag2=mag[1],mag3=mag[2],sc1=score[0],sc2=score[1],sc3=score[2]))