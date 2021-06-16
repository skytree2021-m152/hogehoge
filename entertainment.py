import requests
import pandas as pd
from bs4 import BeautifulSoup

def func(url):
    html=requests.get(url)
    html.encoding = html.apparent_encoding
    soup=BeautifulSoup(html.text,"html.parser")
    #print(soup.prettify)

    #音楽ナタリーサイトの画像説明文削除
    if "natalie.mu" in url:
        for i in range(10):
            try:
                soup.find("p", {"class":"NA_article_img_caption"}).extract()
            except AttributeError:
                break

    #fashionsnapサイトの関連記事削除
    if "fashionsnap.com" in url:
        for i in range(3):
            try:
                soup.find("strong").extract()
            except AttributeError:
                break
    
    if "oricon.co.jp" in url:
            soup.find("div",{"class":"topic-path"}).extract()

    for script in soup(["script", "style"]):
        script.decompose()
    #print(soup)
    text=soup.get_text()
    #print(text)
    lines= [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)
    #print(text)

    #サイトごとにtextを切り出し
    if "eiga.com" in url:
        text = text.split('日 >')[1]
        text = text.split('@eigacomをフォロー')[0]
    
    if "natalie.mu" in url:
        text = text.split('ブックマーク')[1]
        text = text.split('この記事の画像')[0]
        
    if "fashionsnap.com" in url:
        text = text.split('ニュース ►')[1]
        text = text.split('メーカー:')[0]
        if "— ADの後に記事が続きます —" in text:
            text= text.replace("— ADの後に記事が続きます —",'')

    if "mdpr.jp" in url:
        text = text.split('views')[1]
        text = text.split('【Not Sponsored 記事】')[0]
        if "すべての画像をみる" in text:
            text= text.replace("すべての画像をみる",'')

    if "oricon.co.jp" in url:
        #text = text.split('''ホームライフ''')[1]
        text = text.split('コメントする・見る')[0]
        if "【写真】その他の写真を見る" in text:
            text= text.replace("【写真】その他の写真を見る",'')


    return text

print(func("https://www.oricon.co.jp/news/2197007/full/"))