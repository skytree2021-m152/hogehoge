import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://eiga.com/news/20210616/7/")
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
print(text)