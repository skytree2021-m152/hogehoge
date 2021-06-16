import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://sports.yahoo.co.jp/column/detail/202106150012-spnavi")
html.encoding = html.apparent_encoding
soup=BeautifulSoup(html.text,"html.parser")
#print(soup.prettify)
for i in range(5):
        try:
            soup.find("ul", {"class":"linkList"}).extract()
        except AttributeError
            break

for script in soup(["script", "style"]):
    script.decompose()
#print(soup)
text=soup.get_text()
#print(text)
lines= [line.strip() for line in text.splitlines()]
text="\n".join(line for line in lines if line)
# print(text)

aruka1= 'Yahoo!ニュース' in text
aruka2= 'sportsnavi' in text
if aruka1==True:
    text=text.split('JavaScriptの設定を変更する方法はこちら')[1]
    text=text.split('【関連記事】')[0]
elif aruka2==True:
    text=text.split('<![endif]-->')[1]
    text=text.split('【関連リンク】')[0]
    text=text.split('続きはスポーツナビ公式アプリ（無料）で読むことができます。')[]
        # aruka5 = 'JavaScriptの設定を変更する方法はこちら' in text
        # aruka6 = 'トピックス一覧' in text
        # aruka7='【関連記事】' in text
        # aruka8='続きを読む' in text
        # if aruka5==True:
        #     text=text.split(aruka5)[1]
        # elif aruka6==True:
        #     text=text.split('トピックス一覧')[1]
        
        # if aruka7==True:
        #     text = text.split('【関連記事】')[0]
        # elif aruka8==True:
        #     text = text.split('続きを読む')[0]
    print(text)