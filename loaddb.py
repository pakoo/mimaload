# -*- coding: utf-8 -*-
import pprint
import MySQLdb
from MySQLdb.cursors import DictCursor
import time

db=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306,db='tianya')
cur=db.cursor()
#cur.execute("""
#select * from user;
#"""
#)
#print 'user:',cur.fetchall()

def insert_user(name,pwd,email='1'):
    try :
        sql="""insert into user(name,password,email) values (%s,%s,%s)"""%(repr(name),repr(pwd),repr(email))
        #print 'sql:',sql
        cur.execute(sql)
        db.commit()
    except :
        print sql
def parser(filename):
    begin_time=time.time()
    mimi=open(filename,'r')
    data=mimi.readlines()
    print 'data len:',len(data)
    for p in data:
        p=p[:-2]
        p=p.split(' ')
        p=[a for a in p if a]
        if len(p)==2:
            name=p[0]
            pwd=p[1]
            insert_user(name,pwd) 
            #print 'username:',name,'password:',pwd
        elif len(p)==3:
            name=p[0]
            pwd=p[1]
            email=p[2] 
            insert_user(name,pwd,email) 
            #print 'username:',name,'password:',pwd,'email:',email
    print 'total time=',time.time()-begin_time

if __name__ == '__main__':
    #insert_user('test','123456')
    parser('./tianyadb/tianya_1.txt')
