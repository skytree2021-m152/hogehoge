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
                soup.find("h4", {"class":"next-title"}).extract()
            except AttributeError:
                break


    for script in soup(["script", "style"]):
        script.decompose()
    #print(soup)
    text=soup.get_text()
    #print(text)
    lines= [line.strip() for line in text.splitlines()]
    text="\n".join(line for line in lines if line)
        #print(text)
    aruka1='ITmedia' in text
    aruka2='TechCrunch Japan' in text
    aruka3='CNET Japan' in text

        
    if aruka1==True:
            aruka4 = '[ITmedia]' in text      
            if aruka4==True:
                text=text.split('[ITmedia]')[1]
                text=text.split('関連記事')[0]
            
    elif aruka2==True:
            aruka5 = '次の記事' in text
            if aruka5==True:
                text=text.split('次の記事')[1]
                text=text.split('関連記事')[0]

    elif aruka3==True:
            aruka6 = 'クリップ' in text

            if aruka6==True:
                text=text.split('クリップ')[1]
                text=text.split('CNET Japanの記事を毎朝メールでまとめ読み')[0]

    return text