from django.test import TestCase

from datetime import datetime
# Create your tests here.
#from TWFB.settings import MPP_ODS_CONFIG
import pymysql
def test():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='112233..',
        db='twfb',
    )
    cur = conn.cursor()
    cur.execute('''
            select * from mainapp_item;
        ''')
    kk = []
    for row in cur.fetchall():
        kk.append((row[1], row[2], row[3], row[4])) #realname and content
    print(type(row[1]))
    print(kk)
    cur.execute('''
        select * from mainapp_lastpostid;
    ''')
    last_post = []
    for row in cur.fetchall():
        last_post.append(row)
        print(last_post)

    print(row)
    print('Done!')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TWFB.settings")

import django
django.setup()
from datetime import datetime

def write_to_post():

    from mainapp.models import LastPostID
    lpi = LastPostID.objects.all()
    if len(LastPostID.objects.all())==0:
        LastPostID.objects.create(postdt=datetime.today(), postid=1)
        print("have run!")

    for i in range(10):
        length = len(LastPostID.objects.all())
        last = LastPostID.objects.all()[length-1]
        # the last post datetime
        last_dt = last.postdt
        LastPostID.objects.create(postdt=datetime.today(), postid=last.postid + 1)
        print (last_dt)
    print ("End")

if __name__ == "__main__":
    #test()
    #write_to_post()
    res = []
    l1 = [2*i for i in range(10)]
    l2 = [2*i+1 for i in range(10)]
    for x in range(10):
        a = {}
        a.setdefault("item1",l1[x])
        a.setdefault("item2",l2[x])
        res.append(a)
    for x in res:
        print(x['item1'], x['item2'])







