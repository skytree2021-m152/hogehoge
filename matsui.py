import requests
from bs4 import BeautifulSoup

response = requests.get('https://www3.nhk.or.jp/news/html/20210614/k10013083911000.html')
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,'lxml')
title = soup.title.string
print(title)