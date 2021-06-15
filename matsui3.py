import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://www3.nhk.or.jp/news/html/20210615/k10013085681000.html")
html.encoding = html.apparent_encoding
soup=BeautifulSoup(html.text,"html.parser")
#print(soup.prettify)
for script in soup(["script", "style"]):
    script.decompose()
#print(soup)
text=soup.get_text()
#print(text)
lines= [line.strip() for line in text.splitlines()]
text="\n".join(line for line in lines if line)
#print(text)
aruka = 'Yahoo!ニュース' in text
aruka2='NHKニュース' in text
aruka3='[ITmedia]' in text
aruka4='関連記事' in text
#print(aruka)
if aruka==True:
    text = text.split('【関連記事】')[0]
    text = text.split('JavaScriptの設定を変更する方法はこちら')[1]
if aruka2==True:
    text = text.split('社会ニュース一覧へ戻る')[0]
    text = text.split('このページではJavaScriptを使用しています。')[1]
if aruka3==True:
    text = text.split('[ITmedia]')[1]
if aruka4 == True:
    text = text.split('関連記事')[0]
print(text)