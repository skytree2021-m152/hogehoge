#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'TWITTER トレンド'

print('''
Content-type: text/html

<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<title>{title}</title>

</head>

<body>

<h2>{title}<h2> 
<p>ページ説明を入れる予定</p>


<main>
    <section>
      <form action="/cgi-bin/step2.py" method="post">
      <dl>
        <dt>リスト検索</dt><dd><select id="activity" name="activity"><option value="">-----</option><option value="1">IT</option><option value="2">News</option><option value="3">スポーツ</option><option value="4">芸能・エンタメ</option></select></dd>
      </dl>
      <button class="btn">入力</button>
      </form>
    </section>
</main>

</body>
</html>
'''[1:-1].format(title=title_str))