import mytw, mydb, random, os, sys, traceback

if __name__ == '__main__':

    # get target person id
    rose_person_id = os.environ.get('ROSE_PERSON_ID')
    

    #4の目が出やすいように重みを設定する
    w = [1,2,3,4,4,4,5,6]
 
    
    if rose_person_id is None:
        rose_person_id = random.choice(w)
    

    # get twitter id
    twitter_id = os.environ.get('TWITTER_ID')
    if twitter_id is None:
        twitter_id = 'SKYTREE2021_01'
  
    tw = mytw.MyTwitter(twitter_id)
    
    db = mydb.MyDatabase()
  
    conn = db.conn
    cur = conn.cursor()
    row_num = db.count_rows('rose', 'person', rose_person_id)
      
    # get saying
    num = random.randint(0,row_num)
    #sql = "SELECT contents FROM rose WHERE person = {} OFFSET {} LIMIT 1;".format(rose_person_id, num)
    sql = "SELECT p.name, s.contents FROM rose AS s LEFT JOIN rose_person AS p ON s.person = p.id WHERE s.person = {} OFFSET {} LIMIT 1".format(rose_person_id, num)
    
    try:
        cur.execute(sql)
        res = cur.fetchone()
        if res is None:
            name = "その他"
            text = "終焉を知ってなお咲き急ぐ莟のように"
        else:
            name = res[0]
            text = res[1]

        text_all = """【ローゼンメイデン{}の言葉】
{}""".format(name, text)

        print(text_all)
        #tw.api.update_status(text_all)
        

    except:
        traceback.print_exc()
        sys.exit(1) 

