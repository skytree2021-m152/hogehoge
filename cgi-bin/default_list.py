import requests
import pandas as pd
from bs4 import BeautifulSoup

def func(url):
    html=requests.get(url)
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
    aruka ='Yahoo!ニュース' in text
    aruka2='NHKニュース' in text
    aruka3='読売新聞' in text
    aruka4='朝日新聞デジタル記事' in text
    #print(aruka)
    if aruka==True:
        aruka5 = 'JavaScriptの設定を変更する方法はこちら' in text
        aruka6 = 'トピックス一覧' in text
        aruka7='【関連記事】' in text
        aruka8='続きを読む' in text
        if aruka5==True:
            text=text.split('JavaScriptの設定を変更する方法はこちら')[1]
        elif aruka6==True:
            text=text.split('トピックス一覧')[1]
        
        if aruka7==True:
            text = text.split('【関連記事】')[0]
        elif aruka8==True:
            text = text.split('続きを読む')[0]
    
    elif aruka2==True:
        aruka11 = 'このページではJavaScriptを使用しています。' in text
        aruka12 = '一覧へ戻る' in text
        if aruka11==True:
            text=text.split('このページではJavaScriptを使用しています。')[1]
        if aruka12==True:
            text=text.split('一覧へ戻る')[0]
        
        
    elif aruka3==True:
        aruka13 = '完了しました' in text
        aruka14 = 'あわせて読みたい' in text
        if aruka13==True:
            text=text.split('完了しました')[1]
        if aruka14==True:
            text=text.split('あわせて読みたい')[0]

    elif aruka4 == True:
        text = text.split('[PR]')[1]
        aruka9 = 'この記事は有料会員記事です。' in text
        aruka10='関連ニュース' in text
        if aruka9==True:
            text = text.split('この記事は有料会員記事です。')[0]
        elif aruka10==True:
            text = text.split('関連ニュース')[0]

    return text