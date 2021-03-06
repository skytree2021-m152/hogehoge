import requests
import pandas as pd
from bs4 import BeautifulSoup

def func(url):
    html=requests.get(url)
    html.encoding = html.apparent_encoding
    soup=BeautifulSoup(html.text,"html.parser")
    #print(soup.prettify)
    for i in range(3):
        try:
            soup.find("a", {"class":"bbc-n8oauk e1cs6q200"}).extract()
        except AttributeError:
            break
    for script in soup(["script", "style"]):
        script.decompose()
    #print(soup)
    text=soup.get_text()
    #print(text)
    lines= [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)

    if "ロイター" in text:
        if '分で読む' in text:
            text = text.split('分で読む')[1]
        if '私たちの行動規範' in text:
            text = text.split('私たちの行動規範')[0]

    if "BBCニュース" in text:
        if '関連コンテンツ' in text:
            text = text.split('関連コンテンツ')[0]
        if '私たちの行動規範' in text:
            text= text.replace('＜関連記事＞','')
        if 'お使いの端末ではメディアプレイバックはご利用になれません' in text:
            text = text.split('お使いの端末ではメディアプレイバックはご利用になれません')[1]
        if 'ジャンルホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTVホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTV' in text:
            text = text.split('ジャンルホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTVホームコロナウイルス日本アジアイギリスアメリカ解説・読み物ビデオワールドニュースTV')[1]
    return text
