import psycopg2
import json
from datetime import datetime
from psycopg2 import Error
import requests
from bs4 import BeautifulSoup
import urllib3
import re

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    connection.autocommit= True

    with open ('scraped_english_articles.json') as access_json:
        read_content = json.load (access_json)

    newspapers = ['banglatribune']
    for newspaper in newspapers:
        article_list = read_content.get('newspapers').get(newspaper).get('articles')
        for i in article_list:
            values = i.values()
            values_list = list(values)
            listToStr = '~~'.join(map(str, values_list))
            # print(listToStr,'\n')
            l = listToStr.split('~~')

            result = "Link: " + l[0] + \
                     "\nPublished: " + l[1] \
                     + "\nTitle: " + l[2] \
                     + "\nSummary: " + l[3] + "\n"

            dt = l[2]
            dl = l[0]
            dp = l[1]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.date()
            qq = """ INSERT INTO banglatribune (bt_date, bt_published, bt_title , bt_link) VALUES (%s , %s, %s, %s)"""
            tu = (current_date, dp, dt, dl)
            cursor.execute(qq,tu)


    newspapers = ['bbc']
    for newspaper in newspapers:
        article_list = read_content.get('newspapers').get(newspaper).get('articles')
        for i in article_list:
            values = i.values()
            values_list = list(values)
            listToStr = '~~'.join(map(str, values_list))
            # print(listToStr,'\n')
            l = listToStr.split('~~')

            result = "Link: " + l[0] + \
                     "\nPublished: " + l[1] \
                     + "\nTitle: " + l[2] \
                     + "\nSummary: " + l[3] + "\n"

            dt = l[2]
            dl = l[0]
            dp = l[1]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.date()
            qq = """ INSERT INTO bbc (bbc_date, bbc_published, bbc_title , bbc_link) VALUES (%s , %s, %s, %s)"""
            tu = (current_date, dp, dt, dl)
            cursor.execute(qq,tu)

    newspapers = ['thedailystar']
    for newspaper in newspapers:
        article_list = read_content.get('newspapers').get(newspaper).get('articles')
        for i in article_list:
            values = i.values()
            values_list = list(values)
            listToStr = '~~'.join(map(str, values_list))
            # print(listToStr,'\n')
            l = listToStr.split('~~')

            result = "Link: " + l[0] + \
                     "\nPublished: " + l[1] \
                     + "\nTitle: " + l[2] \
                     + "\nSummary: " + l[3] + "\n"

            dt = l[2]
            dl = l[0]
            dp = l[1]
            now = datetime.now()
            # current_time = now.strftime("%H:%M:%S")
            # current_date = now.date()

            tits = now.strftime ( "%H:%M:%S" )

            current_time = tits [ 0:5 ]
            current_date = now.date ( )
            # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
            # tu = (current_date, dp, dt, dl)
            # cursor.execute(qq,tu)

            qq = """ INSERT INTO testtable (tt_date, tt_time, tt_published, tt_title , tt_link) VALUES (%s ,%s, %s, %s, %s)"""
            tu = (current_date , current_time, dp , dt , dl)
            cursor.execute ( qq , tu )

##########################prothom alo####################
            url = "https://prod-qt-images.s3.amazonaws.com/production/prothomalo-bangla/feed.xml"
            resp = requests.get (url , headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

            soup = BeautifulSoup (resp.content , features="xml")
            entrys = soup.findAll ("entry")

            for i in range (20):
                entry = entrys [ i ]
                title = entry.title.text
                summary = entry.summary.text
                ss = entry.link [ 'href' ]
                publish = entry.published.text
                category = entry.category [ 'term' ]

                if (
                        category == "ক্রিকেট" or category == "fun" or category == "বলিউড" or category == "টেলিভিশন" or category == "খেলা" or category == "নিয়োগ" or category == "উচ্চশিক্ষা"
                        or category == "টেনিস" or category == "অন্য খেলা" or category == "লাইভ স্কোর" or category == "ফুটবল" or category == "সাক্ষাৎকার"
                        or category == "লাইফস্টাইল" or category == "ফ্যাশন" or category == "স্টাইল" or category == "ফুটবল" or category == "রূপচর্চা" or category == "গৃহসজ্জা" or category == "রসনা" or category == "কেনাকাটা"
                        or category == "বিনোদন" or category == "ঢালিউড" or category == "আলাপন" or category == "নাটক" or category == "গান" or category == "হলিউড"
                        or category == "kishoralo" or category == "golpo" or category == "প্র স্বাস্থ্য"
                ):
                    continue
                else:
                    result = "Title: " + title + \
                             "\nSummary: " + summary \
                             + "\nLink: " + ss \
                             + "\nPublished: " + publish \
                             + "\nCategory: " + category + "\n"


                    # print(result)
                    now = datetime.now ()

                    now = datetime.now ()

                    tits = now.strftime("%H:%M:%S")

                    current_time = tits[0:5]
                    current_date = now.date ()

                    qq = """ INSERT INTO prothomalo (pa_date, pa_published, pa_title , pa_link) VALUES (%s , %s, %s, %s)"""
                    tu = (current_date , publish , title , ss)
                    cursor.execute (qq , tu)

                    # current_time = now.strftime ("%H:%M:%S")
                    # l = current_time.split (':')
                    #
                    # current_hour = l [ 0 ]
                    # current_min = l [ 1 ]
            #
            # for i in range (6):
            #     entry = entrys [ i ]
            #     title = entry.title.text
            #     summary = entry.summary.text
            #     ss = entry.link [ 'href' ]
            #     publish = entry.published.text
            #
            #     result = "Title: " + title + \
            #              "\nSummary: " + summary \
            #              + "\nLink: " + ss \
            #              + "\nPublished: " + publish + "\n"

                # print (result)
                #

    # # Create a cursor to perform database operations
    # cursor = connection.cursor()
    #
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # current_date = now.date()
    #
    # q = 'create table bbc (id serial, date date, title varchar(255), link varchar(255));'
    # # q2 = 'insert into bbc (date, title , link ) values (current_date, 'Democrats introduce Trump impeachment article in House','https://www.thedailystar.net/online/news/democrats-introduce-trump-impeachment-article-house-2026029'');'
    # q2 = """ INSERT INTO bbc (date, title , link) VALUES (current_date, 'Iphone12', 'https://pynative.com/python-postgresql-tutorial/')"""
    # d = 'drop table bbc'
    # f = """select * from bbc"""
    # cursor.execute(f)

    # q = 'create table bbc (bbc_id serial , bbc_date date, bbc_published varchar(255), bbc_title varchar(255), bbc_link varchar(255), constraint bbc_id_pk primary key (bbc_id));'
    # q2 = 'create table dailystar (ds_id serial , ds_date date, ds_published varchar(255), ds_title varchar(255), ds_link varchar(255), constraint ds_id_pk primary key (ds_id));'
    # q3 = 'create table banglatribune (bt_id serial , bt_date date, bt_published varchar(255), bt_title varchar(255), bt_link varchar(255), constraint bt_id_pk primary key (bt_id));'
    # #
    # #
    # # # d = ("drop table dailystar")
    # # # d1= ("drop table bbc")
    # # # d2=("drop table banglatribune")
    # cursor.execute(q3)
    # cursor.execute(q2)
    # cursor.execute(d2)


    connection.commit()
    print("Inserted successfully in PostgreSQL ")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
