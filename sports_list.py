import requests
import pandas as pd
from bs4 import BeautifulSoup


    html=requests.get('https://news.yahoo.co.jp/articles/794efb16ebbe204b1536e4a026468e59db10cf96')
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
    aruka1='Yahoo!ニュース' in text
    
   
    if aruka1==True:
        text = text.split()[0]
     
    print(text)