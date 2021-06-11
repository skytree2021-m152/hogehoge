import mytw, mydb, random, os, sys, traceback

if __name__ == '__main__':

    # get target person id
    saying_person_id = os.environ.get('SAYING_PERSON_ID')
    if saying_person_id is None:
        saying_person_id = 2

    # get twitter id
    twitter_id = os.environ.get('TWITTER_ID')
    if twitter_id is None:
        twitter_id = 'SKYTREE2021_01'

    tw = mytw.MyTwitter(twitter_id)
    db = mydb.MyDatabase()
    conn = db.conn
    cur = conn.cursor()

    row_num = db.count_rows('saying', 'person', saying_person_id)

    # get saying
    num = random.randint(0,row_num)
    #sql = "SELECT contents FROM saying WHERE person = {} OFFSET {} LIMIT 1;".format(saying_person_id, num)
    sql = "SELECT p.name, s.contents FROM saying AS s LEFT JOIN saying_person AS p ON s.person = p.id WHERE s.person = {} OFFSET {} LIMIT 1".format(saying_person_id, num)
    try:
        cur.execute(sql)
        res = cur.fetchone()
        if res is None:
            name = "般若心経"
            text = "色即是空空即是色"
        else:
            name = res[0]
            text = res[1]

        text_all = """【{}のありがたいお言葉bot】
{}""".format(name, text)
        #print(text_all)
        tw.api.update_status(text_all)

    except:
        traceback.print_exc()
        sys.exit(1)

