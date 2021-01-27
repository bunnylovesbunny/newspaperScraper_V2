import psycopg2
import json
from datetime import datetime
from psycopg2 import Error
import requests
from bs4 import BeautifulSoup
import urllib3
import re

with open('scraped_english_articles.json') as access_json:
    read_content = json.load(access_json)

now = datetime.now()
tits = now.strftime("%H:%M:%S")

current_time = tits[0:5]
current_date = now.date()


def insert():
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")


    cur=connection.cursor()
    newspapers = [ 'bbc' ]

    #### newspaper iteration
    for newspaper in newspapers:
        article_list = read_content.get('newspapers').get(newspaper).get('articles')
        for i in article_list:
            values = i.values( )
            values_list = list(values)
            listToStr = '~~'.join(map(str , values_list))
            # print(listToStr,'\n')
            l = listToStr.split('~~')

            # result = "Link: " + l [ 0 ] + \
            #          "\nPublished: " + l [ 1 ] \
            #          + "\nTitle: " + l [ 2 ] \
            #          + "\nSummary: " + l [ 3 ] + "\n"

            dt = l [ 2 ]
            dl = l [ 0 ]
            dp = l [ 1 ]
            ds = l [ 3 ]
            # current_time = now.strftime("%H:%M:%S")
            # current_date = now.date()

            # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
            # tu = (current_date, dp, dt, dl)
            # cursor.execute(qq,tu)
            # print("before insertion")

            qq = """ INSERT INTO bbc (bbc_date, bbc_time, bbc_published, bbc_title , bbc_link, bbc_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
            tu = (current_date , current_time , dp , dt , dl , ds)
            cur.execute(qq , tu)

            # qq = """ INSERT INTO sendbbc (sendbbc_date, sendbbc_time, sendbbc_published, sendbbc_title , sendbbc_link, sendbbc_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
            # tu = (current_date, current_time, dp, dt, dl, ds)
            # cur.execute(qq, tu)

            # print("Inserted")


    connection.commit()
    connection.close()
    viewbbc()

def viewbbc():
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("SELECT * FROM bbc")
    row=cur.fetchall()
    connection.close()
    return row

def viewprothomalo():
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("SELECT * FROM prothomalo")
    row=cur.fetchall()
    connection.close()
    return row

def viewdailystar():
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("SELECT * FROM dailystar")
    row=cur.fetchall()
    connection.close()
    return row

def search(published="",date="",title="",link=""):
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("SELECT * FROM bbc WHERE bbc_published=? OR bbc_date=? OR bbc_title=?  OR  bbc_link=?",(published,date,title,link))
    row=cur.fetchall()
    connection.close()
    return row

def delete(id):
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("DELETE FROM bbc  where id=?",(id,))
    connection.commit()
    connection.close()

def update(id,name,address,phone_number,room_type,no_of_days,total):
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cur=connection.cursor()
    cur.execute("UPDATE bbc SET name=? ,address=? , phone_number=? ,  room_type=? , no_of_days=? , total=? where id=?",(name,address,phone_number,room_type,no_of_days,calculation(no_of_days,room_type),id))
    connection.commit()
    connection.close()

def sendlist():
    numbers = []
    f = open("numbers.txt", "r")
    for line in f.read().splitlines():
        if line != "":
            numbers.append(line)
    f.close()
    # total_number = len(numbers)
    return numbers