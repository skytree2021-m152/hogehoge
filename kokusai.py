import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.bbc.com/japanese/57478973"
html=requests.get(url)
html.encoding = html.apparent_encoding
soup=BeautifulSoup(html.text,"html.parser")
#print(soup.prettify)
for i in range(3):
    soup.find("a", {"class":"bbc-n8oauk e1cs6q200"}).extract()
for script in soup(["script", "style"]):
    script.decompose()
#print(soup)
text=soup.get_text()
#print(text)
lines= [line.strip() for line in text.splitlines()]
text="\n".join(line for line in lines if line)

if "ロイター" in text:
    text = text.split('1 分で読む')[1]
    text = text.split('私たちの行動規範')[0]

if "BBCニュース" in text:
    text = text.split('関連コンテンツ')[0]
    text= text.replace('＜関連記事＞','')
    if 'お使いの端末ではメディアプレイバックはご利用になれません' in text:
        text = text.split('お使いの端末ではメディアプレイバックはご利用になれません')[1]
    if 'ジャンルホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTVホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTV' in text:
        text = text.split('ジャンルホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTVホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTV')[1]
print(text)
