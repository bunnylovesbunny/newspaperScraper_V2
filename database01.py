import psycopg2
import json
from datetime import datetime
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()

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
            current_time = now.strftime("%H:%M:%S")
            current_date = now.date()
            qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
            tu = (current_date, dp, dt, dl)
            cursor.execute(qq,tu)








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
