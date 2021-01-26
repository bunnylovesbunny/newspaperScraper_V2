
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

    # with open ('scraped_english_articles.json') as access_json:
    #     read_content = json.load (access_json)
    #
    # newspapers = ['thedailystar']
    # for newspaper in newspapers:
    #     article_list = read_content.get('newspapers').get(newspaper).get('articles')
    #     for i in article_list:
    #         values = i.values()
    #         values_list = list(values)
    #         listToStr = '~~'.join(map(str, values_list))
    #         # print(listToStr,'\n')
    #         l = listToStr.split('~~')
    #
    #         result = "Link: " + l[0] + \
    #                  "\nPublished: " + l[1] \
    #                  + "\nTitle: " + l[2] \
    #                  + "\nSummary: " + l[3] + "\n"
    #
    #         dt = l[2]
    #         dl = l[0]
    #         now = datetime.now()
    #         current_time = now.strftime("%H:%M:%S")
    #         current_date = now.date()
    #         qq = """ INSERT INTO bbc (date, title , link) VALUES (%s , %s, %s)"""
    #         tu = (current_date, dt, dl)
    #         # cursor.execute(qq,tu)
    #
    #         q = 'create table thedailystar (ds_id serial , ds_date date, ds_published varchar(255), ds_title varchar(255), ds_link varchar(255), constraint daily_star_id_pk primary key (ds_id));'
    #         d = 'drop table bbc'

    duplicate_query1 = 'delete from banglatribune b1 using banglatribune b2 where b1.bt_id < b2.bt_id and b1.bt_title = b2.bt_title '
    cursor.execute (duplicate_query1)

    duplicate_query2 = 'delete from bbc b1 using bbc b2 where b1.bbc_id < b2.bbc_id and b1.bbc_title = b2.bbc_title '
    cursor.execute (duplicate_query2)

    duplicate_query3 = 'delete from dailystar b1 using dailystar b2 where b1.ds_id < b2.ds_id and b1.ds_title = b2.ds_title '
    cursor.execute (duplicate_query3)

    duplicate_query4 = 'delete from prothomalo b1 using prothomalo b2 where b1.pa_id < b2.pa_id and b1.pa_title = b2.pa_title '
    cursor.execute (duplicate_query4)





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




    connection.commit()
    print("Duplicated Removed successfully in PostgreSQL ")


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")