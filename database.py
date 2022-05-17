import mysql.connector
from datetime import date
from flask import flash
mydb=mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)
mycursor=mydb.cursor()

def check_user(user_id,passwod):
    check_record = "select passwd from users where userid=%s"
    user_id=[user_id]
    mycursor.execute(check_record, user_id)
    try:
        l=mycursor.fetchall()[0][0]
    except:
        return False
    if passwod ==l:
        return True
    else:
        return False

def add_user(user_id,passwd):
    try:
        v=(user_id, passwd)
        add_record="insert into users (userid,passwd) values(%s,%s)"
        mycursor.execute(add_record,v)
        mydb.commit()
        return True
    except:
        return False

def add_post(user,post):
    today=date.today()
    today=today.strftime("%d-%m-%Y")
    count="select count(userid) from posts where userid=(%s)"
    v=(user,)
    mycursor.execute(count,v)

    for i in mycursor:
        n = i[0]
        break
    postid = str(n) + user
    v=(user,postid,post,0,today)
    add_record = "insert into posts (userid,postid,post,likes,date) values(%s,%s,%s,%s,%s)"
    mycursor.execute(add_record, v)
    mydb.commit()

def show_posts():
    mycursor.execute("select * from posts order by likes desc")
    l=[]
    for i in mycursor:
        l.append(list(i))

    return l

def user_posts(user):
    v=(user,)
    q="select * from posts where userid=%s"
    mycursor.execute(q,v)
    l=[]
    for i in mycursor:
        l.append(list(i))

    return l

def today_posts():
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    v=(today,)
    q="select * from posts where date=%s"
    mycursor.execute(q,v)
    l=[]
    for i in mycursor:
        l.append(list(i))

    return l


def add_like(postid):
    v=(postid,)
    q="select likes from posts where postid=%s"
    mycursor.execute(q,v)
    print(mycursor)
    n=0
    for i in mycursor:
        print(i)
        n=int(i[0])+1
        break
    print("noo of likes",n)
    q="update posts set likes=%s where postid=%s"
    v=(n,postid)
    mycursor.execute(q,v)
    mydb.commit()
