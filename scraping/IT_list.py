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
    aruka2='次の記事' in text
    aruka3='ITmedia' in text
    aruka4='関連記事' in text
    aruka5='CNET Japan' in text
    
    if aruka2==True:
        text = text.split('次の記事')[1]
    if aruka3==True:
        text = text.split('[ITmedia]')[1]
        text = text.split('STUDIO >')[1]
    if aruka4 == True:
        text = text.split('関連記事')[0]
    if aruka5 == True:
        text = text.split('クリップ')[1]
        text = text.split('CNET Japan')[0]
    return text