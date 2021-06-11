'''
mydb.py PostgreSQLのテーブルに接続するプログラムのためのクラス定義
        PostgreSQLデータベースに接続できない場合はSQLite3を使う
        jmaテーブル初期化コンストラクタ含む
'''

import psycopg2, os, sys, configparser, traceback
from psycopg2.extras import DictCursor
from requests.packages.urllib3.exceptions import InsecureRequestWarning

CONF_FILE   = 'db.ini'

class MyDatabase:

    conn = None  # コネクション

    def __init__(self):

        config = configparser.ConfigParser()

        # PostgreSQLデータベース操作
        if os.path.exists(CONF_FILE):
            config.read(CONF_FILE)
            db = config['DATABASE']

            try:
                self.conn = psycopg2.connect('dbname={dbname} host={host} user={user} password={password}'.format(dbname=db['dbname'], host=db['dbhost'], user=db['dbuser'], password='P@ssw0rd123###'))
                cur = self.conn.cursor()

            except:
                print(traceback.format_exc())
                sys.exit(1)


    def count_rows(self, tbl=None, key=None, val=0):

        config = configparser.ConfigParser()

        if os.path.exists(CONF_FILE):
            config.read(CONF_FILE)
            default = config['DEFAULT']

            if tbl is None:
                tbl = default['table']

            if key is None:
                cond = ''
            else:
                cond = "WHERE {} = {}".format(key, val)

            sql = "SELECT COUNT(*) FROM {} {}".format( tbl, cond )

            try:
                cur = self.conn.cursor()
                cur.execute(sql)
                res = cur.fetchone()
                if res is None:
                    return 0
                else:
                    return res[0]

            except:
                print(traceback.format_exc())
                sys.exit(1)

        return 0
