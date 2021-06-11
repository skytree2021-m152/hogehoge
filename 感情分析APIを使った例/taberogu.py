#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi, requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main(content, access_token):
    url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key={}'.format(access_token)
    header = {'Content-Type': 'application/json'}
    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": content
        },
        "encodingType": "UTF8"
    }
    res = requests.post(url, headers=header, json=body).json()
    return res


title_str = 'レビュー解析'
form = cgi.FieldStorage()
review = form["review"].value


result = main(review, "AIzaSyAzX7s-hgiekJ7KzSJvfI2yoElbEcZrpLM")
sentence = result['sentences'][0]['text']['content']
score = result['sentences'][0]['sentiment']['score']
magnitude = result['sentences'][0]['sentiment']['magnitude']

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
  <p>ネガポジ値(-1～1)は{score}
  <br>感情の大きさは{magnitude}です。</p>
  <p>分析したレビュー：{sentence}</p>
 </body>
</html>
'''[1:-1].format(title=title_str,score=score,magnitude=magnitude,sentence=sentence))

