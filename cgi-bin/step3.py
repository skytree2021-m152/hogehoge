#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random, cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
params = ['gender', 'age', 'activity']
r = {}
for p in params:
    if p in form:
        r[p] = form[p].value
    else:
        r[p] = '(なし)'

title_str = 'CGIサンプル Step3'

print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
<head>
    <link rel="stylesheet" href="https://andybrewer.github.io/mvp/mvp.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <meta charset="utf-8">
    <meta name="description" content="{title}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>

<body>
  <header>
    <h1>{title}</h1>
  </header>

  <main>
    <section>
      <form action="/cgi-bin/step3.py" method="post">
      <dl>
        <dt>性別</dt><dd>{gender}</dd>
        <dt>年齢</dt><dd>{age}</dd>
        <dt>活動量</dt><dd>{activity}</dd>
      </dl>
      <div>値がちゃんと渡されています</div>
      <!-- ここから以下３行を各Pythonファイルに入れることで次々とデータを渡せます -->
      <input type="hidden" name="gender" value="{gender}"/>
      <input type="hidden" name="age" value="{age}"/>
      <input type="hidden" name="activity" value="{activity}"/>
      <button class="btn">次へ</button>
      </form>
    </section>
  </main>

<script>
$(function() {{
}});
</script>
</body>
</html>
'''[1:-1].format(title=title_str,gender=r['gender'],age=r['age'],activity=r['activity']))
