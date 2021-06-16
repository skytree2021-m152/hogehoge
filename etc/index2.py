#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random
import mytw, tweepy, traceback,datetime
import requests, datetime, json, os, sys, psycopg2, traceback, configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import kanjou
import scraping.default as s

# InsecureRequestWarning対策
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


tw = mytw.MyTwitter()
idlist=[]
umekomi=[]
geturl = "https://api.twitter.com/1.1/statuses/oembed.json?id="

if tw.api is not None:
  #リストの中から最新3ツイートを取得(リツイートを含む)
    for status in tw.api.list_timeline(list_id=1403224831550648321, count=3, include_rts=1):
        #print(status._json["entities"]["urls"][0]["url"])--エラーでる
        #返ってきたtweetのidを取得
        tweet_id = status.id
        idlist.append(tweet_id)


else:
    print(traceback.format_exc())

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
    res=res["html"]
    umekomi.append(res)

#umekomiを確認(いらなくなったら#つけてください)
#print(umekomi)


for i in range(len(statuses)):

  #urlのあるツイートか判定
  if statuses[i]["entities"]["urls"]:
    #ツイートに載っているリンクURLを変数に代入
    url=statuses[i]["entities"]["urls"][0]["url"]
    #urlを別ファイルに渡して実行
    text = default.func(url)
    #print(text)
    texts.append(text)

  else:
    #ツイートの本文取得
    #print(statuses[i]["full_text"])
    texts.append(statuses[i]["full_text"])

#３つのツイートを感情分析APIに入れる
for i in range(3):
  res = kanjou.main(texts[i])
  #CGIの時は↓はけすこと
  #print[res] 

title_str = 'TWITTER トレンド'

print('''
Content-type: text/html

<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">


<link rel="stylesheet" href="index2.css">
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
<h2>感情のデカさ：ほげ1<br>いい話度：hoge1</h2></div>
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
<h2>感情のデカさ：ほげ2<br>いい話度：hoge2</h2></div>
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
<h2>感情のデカさ：ほげ3<br>いい話度：hoge3</h2></div>
</div>
</div>
</div>



<main>
    <section>
      <form action="/cgi-bin/step2.py" method="post"><center>
      <dl>
        <dt>リスト検索</dt><dd><select id="activity" name="activity"><option value="">-----</option><option value="1">IT</option><option value="2">News</option><option value="3">スポーツ</option><option value="4">芸能・エンタメ</option></select></dd>
      </dl>
      <button>入力</button></center>
      </form>
    </section>
</main>

</body>
</html>
'''[1:-1].format(title=title_str,tw1=umekomi[0],tw2=umekomi[1],tw3=umekomi[2]))