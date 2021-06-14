#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, codecs, random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'CGIサンプル Step1'

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
      <form action="/cgi-bin/step2.py" method="post">
      <dl>
        <dt>性別</dt><dd><input type="radio" id="gender" name="gender" value="1"/>女性<input type="radio" name="gender" value="2"/>男性</dd>
        <dt>年齢</dt><dd><input type="range" id="age_bar" name="age_bar" min="16" max="100" step="1" value="25"/><input type="number" id="age" name="age" min="16" max="100"/></dd>
        <dt>活動量</dt><dd><select id="activity" name="activity"><option value="">-----</option><option value="1">高</option><option value="2">中</option><option value="3">低</option></select></dd>
      </dl>
      <button class="btn">入力</button>
      </form>
    </section>
  </main>

<script>
$(function() {{
  var age = $('#age_bar').val();
  console.log(age);
  $('#age').val(age);

  $('#age_bar').on('change', function() {{
    var age = $('#age_bar').val();
    $('#age').val(age);
  }});

  $('#age').on('change', function () {{
    var age = $('#age').val();
    $('#age_bar').val(age);
  }});
}});
</script>
</body>
</html>
'''[1:-1].format(title=title_str))
