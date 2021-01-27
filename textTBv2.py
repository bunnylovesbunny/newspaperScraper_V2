import psycopg2
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException , UnexpectedAlertPresentException , NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import urllib3
import re


try:
    # options = Options ( )
    # options.add_argument('--user-data-dir=./User_Data')
    # driver = webdriver.Chrome("drivers\\chromedriver.exe" , options=options)
    # driver.get('https://web.whatsapp.com')

    connection = psycopg2.connect ( user="postgres" ,
                                    password="123456" ,
                                    host="127.0.0.1" ,
                                    port="5432" ,
                                    database="postgres" )
    cursor = connection.cursor ( )

    ##### fetch data from json file
    with open ('scraped_english_articles.json') as access_json:
        read_content = json.load (access_json)

    now = datetime.now ( )
    tits = now.strftime ( "%H:%M:%S" )

    current_time = tits [ 0:5 ]
    current_date = now.date ( )

    #------------------------------------------- task for daily star ---------------------------------------------------------#

    newspapers = ['bbc']

    #### newspaper iteration
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
            ds = l[3]
            status = 'unsent'
            # current_time = now.strftime("%H:%M:%S")
            # current_date = now.date()


            # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
            # tu = (current_date, dp, dt, dl)
            # cursor.execute(qq,tu)
            #print("before insertion")

            qq = """ INSERT INTO testtable (tt_date, tt_time, tt_published, tt_title , tt_link,send_status) VALUES (%s ,%s, %s, %s, %s, %s)"""
            tu = (current_date , current_time, dp , dt , dl, status)
            cursor.execute ( qq , tu )



            # qq = """ INSERT INTO senddailystar (sendds_date, sendds_time, sendds_published, sendds_title , sendds_link, sendds_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
            # tu = (current_date , current_time , dp , dt , dl , ds)
            # cursor.execute(qq , tu)

           # print("Inserted")

            # duplicate_query3 = 'delete from testtable b1 using testtable b2 where b1.tt_id < b2.tt_id and b1.tt_title = b2.tt_title'
            # cursor.execute ( duplicate_query3 )
            # print ("Removed duplicates")

    count_query = "select count (*) from testtable where tt_time = '%s'" % current_time
    cursor.execute(count_query)
    (number_of_row,)=cursor.fetchone()
    print(number_of_row)
    ##fetch common data

    duplicate_query = 'delete from testtable b1 using testtable b2 where b1.tt_id < b2.tt_id and b1.tt_title = b2.tt_title'
    cursor.execute(duplicate_query)
    print("Removed duplicates")
    # # ##### fetch from database
    postgreSQL_select_Query = ("select * from testtable where tt_time= '%s'" %current_time)

    cursor.execute ( postgreSQL_select_Query)



    # print ( "Selecting rows from mobile table using cursor.fetchall" )
    mobile_records = cursor.fetchall ( )



    # print ( "Messages daily star are being send" )
    # for row in mobile_records:
    #     # print ( "Id = " , row [ 0 ] , )
    #     # print ( "Date = " , row [ 1 ] )
    #     # print ( "Time  = " , row [ 2 ]  )
    #     # print ( "Published = " , row [ 3 ] )
    #     # print ( "Title  = " , row [ 4 ]  )
    #     # print ("Link = ", row[ 5 ], "\n")
    #
    #     message = "Link: " + row [ 5 ] + \
    #               "\nPublished: " + row [ 3 ] \
    #               + "\nTitle: " + row [ 4 ] \
    #               + "\nSummary: " + row [6] \
    #               + "\n"
    #     sleep(10)
    #     print ( 'This is your message..' )
    #     print ( message )
    #     message = quote ( message )
    #     numbers = [ ]
    #     f = open ( "numbers.txt" , "r" )
    #     for line in f.read ( ).splitlines ( ):
    #         if line != "":
    #             numbers.append ( line )
    #     f.close ( )
    #     total_number = len ( numbers )
    #
    #     print ( '\nWe found ' + str ( total_number ) + ' numbers in the file' )
    #     delete_news = ("delete from dailystar where ds_title= '%s'" % row[4])
    #     cursor.execute(delete_news)
    #     print ( )
    #     delay = 30
    #
    #     # if platform == "win32":
    #     #
    #     # else:
    #     #     driver = webdriver.Chrome ( "./drivers/chromedriver" , options=options )
    #     print ( 'Once your browser opens up sign in to web whatsapp' )
    #     sleep ( 20 )
    #     # input ( "Press ENTER after login into Whatsapp Web and your chats are visiable	." )
    #     for idx , number in enumerate ( numbers ):
    #         if number == "":
    #             continue
    #         print ( '{}/{} => Sending message to {}.'.format ( (idx + 1) , total_number , number ) )
    #         try:
    #             url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
    #             driver.get ( url )
    #             try:
    #                 click_btn = WebDriverWait ( driver , delay ).until (
    #                     EC.element_to_be_clickable ( (By.CLASS_NAME , '_2Ujuu') ) )
    #             except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
    #                 print ( "alert present" )
    #                 Alert ( driver ).accept ( )
    #             sleep ( 1 )
    #             click_btn.click ( )
    #             sleep ( 3 )
    #             print ( 'Message sent to: ' + number )
    #         except Exception as e:
    #             print ( 'Failed to send message to ' + number + str ( e ) )
    #


    #-----------------------------------------------task for banglaTribune------------------------------------------------------------#

    # ------------------------------------------- task for bangla tribune ---------------------------------------------------------#
    # sleep(10)
    # newspapers = ['banglatribune']
    #
    # #### newspaper iteration
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
    #         dp = l[1]
    #         ds = l[3]
    #         # current_time = now.strftime("%H:%M:%S")
    #         # current_date = now.date()
    #
    #
    #         # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
    #         # tu = (current_date, dp, dt, dl)
    #         # cursor.execute(qq,tu)
    #         print("before insertion")
    #
    #         qq = """ INSERT INTO banglatribune (dt_date, dt_time, dt_published, dt_title , dt_link, dt_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
    #         tu = (current_date , current_time, dp , dt , dl,ds)
    #         cursor.execute ( qq , tu )
    #
    #         print("Inserted")
    #
    #         duplicate_query3 = 'delete from banglatribune b1 using banglatribune b2 where b1.dt_id < b2.dt_id and b1.dt_title = b2.dt_title '
    #         cursor.execute ( duplicate_query3 )
    #         print ("Removed duplicates")
    #
    #     # # ##### fetch from database
    # postgreSQL_select_Query = ("select * from banglatribune where dt_time= '%s'" % current_time)
    #
    # cursor.execute(postgreSQL_select_Query)
    # # print ( "Selecting rows from mobile table using cursor.fetchall" )
    # mobile_records = cursor.fetchall( )
    #
    # print("Messages from bangla tribune are being send")
    # for row in mobile_records:
    #     # print ( "Id = " , row [ 0 ] , )
    #     # print ( "Date = " , row [ 1 ] )
    #     # print ( "Time  = " , row [ 2 ]  )
    #     # print ( "Published = " , row [ 3 ] )
    #     # print ( "Title  = " , row [ 4 ]  )
    #     # print ("Link = ", row[ 5 ], "\n")
    #
    #     message = "Link: " + row [ 5 ] + \
    #               "\nPublished: " + row [ 3 ] \
    #               + "\nTitle: " + row [ 4 ] \
    #               + "\nSummary: " + row [ 6 ] \
    #               + "\n"
    #     sleep(10)
    #     print('This is your message..')
    #     print(message)
    #     message = quote(message)
    #     numbers = [ ]
    #     f = open("numbers.txt" , "r")
    #     for line in f.read( ).splitlines( ):
    #         if line != "":
    #             numbers.append(line)
    #     f.close( )
    #     total_number = len(numbers)
    #
    #     print('\nWe found ' + str(total_number) + ' numbers in the file')
    #
    #     print( )
    #     delay = 30
    #
    #     # if platform == "win32":
    #     #
    #     # else:
    #     #     driver = webdriver.Chrome ( "./drivers/chromedriver" , options=options )
    #     print('Once your browser opens up sign in to web whatsapp')
    #     sleep(20)
    #     # input ( "Press ENTER after login into Whatsapp Web and your chats are visiable	." )
    #     for idx , number in enumerate(numbers):
    #         if number == "":
    #             continue
    #         print('{}/{} => Sending message to {}.'.format((idx + 1) , total_number , number))
    #         try:
    #             url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
    #             driver.get(url)
    #             try:
    #                 click_btn = WebDriverWait(driver , delay).until(
    #                     EC.element_to_be_clickable((By.CLASS_NAME , '_2Ujuu')))
    #             except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
    #                 print("alert present")
    #                 Alert(driver).accept( )
    #             sleep(1)
    #             click_btn.click( )
    #             sleep(3)
    #             print('Message sent to: ' + number)
    #         except Exception as e:
    #             print('Failed to send message to ' + number + str(e))

      #--------------------------------------- task for bbc --------------------------------------------------------------#
    # sleep(10)
    # newspapers = [ 'bbc' ]
    #
    # #### newspaper iteration
    # for newspaper in newspapers:
    #     article_list = read_content.get('newspapers').get(newspaper).get('articles')
    #     for i in article_list:
    #         values = i.values( )
    #         values_list = list(values)
    #         listToStr = '~~'.join(map(str , values_list))
    #         # print(listToStr,'\n')
    #         l = listToStr.split('~~')
    #
    #         result = "Link: " + l [ 0 ] + \
    #                  "\nPublished: " + l [ 1 ] \
    #                  + "\nTitle: " + l [ 2 ] \
    #                  + "\nSummary: " + l [ 3 ] + "\n"
    #
    #         dt = l [ 2 ]
    #         dl = l [ 0 ]
    #         dp = l [ 1 ]
    #         ds = l [ 3 ]
    #         # current_time = now.strftime("%H:%M:%S")
    #         # current_date = now.date()
    #
    #         # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
    #         # tu = (current_date, dp, dt, dl)
    #         # cursor.execute(qq,tu)
    #         print("before insertion")
    #
    #         qq = """ INSERT INTO bbc (bbc_date, bbc_time, bbc_published, bbc_title , bbc_link, bbc_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
    #         tu = (current_date , current_time , dp , dt , dl , ds)
    #         cursor.execute(qq , tu)
    #
    #         print("Inserted")
    #
    #         duplicate_query3 = 'delete from bbc b1 using bbc b2 where b1.bbc_id < b2.bbc_id and b1.bbc_title = b2.bbc_title '
    #         cursor.execute(duplicate_query3)
    #         print("Removed duplicates")
    #
    #         # # ##### fetch from database
    #     postgreSQL_select_Query = ("select * from bbc where bbc_time= '%s'" % current_time)
    #
    #     cursor.execute(postgreSQL_select_Query)
    #     # print ( "Selecting rows from mobile table using cursor.fetchall" )
    #     mobile_records = cursor.fetchall( )
    #
    #     print("Messages from bbc being send")
    #     for row in mobile_records:
    #         # print ( "Id = " , row [ 0 ] , )
    #         # print ( "Date = " , row [ 1 ] )
    #         # print ( "Time  = " , row [ 2 ]  )
    #         # print ( "Published = " , row [ 3 ] )
    #         # print ( "Title  = " , row [ 4 ]  )
    #         # print ("Link = ", row[ 5 ], "\n")
    #
    #         message = "Link: " + row [ 5 ] + \
    #                   "\nPublished: " + row [ 3 ] \
    #                   + "\nTitle: " + row [ 4 ] \
    #                   + "\nSummary: " + row [ 6 ] \
    #                   + "\n"
    #         sleep(10)
    #         print('This is your message..')
    #         print(message)
    #         message = quote(message)
    #         numbers = [ ]
    #         f = open("numbers.txt" , "r")
    #         for line in f.read( ).splitlines( ):
    #             if line != "":
    #                 numbers.append(line)
    #         f.close( )
    #         total_number = len(numbers)
    #
    #         print('\nWe found ' + str(total_number) + ' numbers in the file')
    #
    #         print( )
    #         delay = 30
    #
    #         # if platform == "win32":
    #         #
    #         # else:
    #         #     driver = webdriver.Chrome ( "./drivers/chromedriver" , options=options )
    #         print('Once your browser opens up sign in to web whatsapp')
    #         sleep(20)
    #         # input ( "Press ENTER after login into Whatsapp Web and your chats are visiable	." )
    #         for idx , number in enumerate(numbers):
    #             if number == "":
    #                 continue
    #             print('{}/{} => Sending message to {}.'.format((idx + 1) , total_number , number))
    #             try:
    #                 url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
    #                 driver.get(url)
    #                 try:
    #                     click_btn = WebDriverWait(driver , delay).until(
    #                         EC.element_to_be_clickable((By.CLASS_NAME , '_2Ujuu')))
    #                 except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
    #                     print("alert present")
    #                     Alert(driver).accept( )
    #                 sleep(1)
    #                 click_btn.click( )
    #                 sleep(3)
    #                 print('Message sent to: ' + number)
    #             except Exception as e:
    #                 print('Failed to send message to ' + number + str(e))
    #
    #     #-------------------------------------task for prothomalo -------------------------------------------#
    # # sleep(10)
    # # url = "https://prod-qt-images.s3.amazonaws.com/production/prothomalo-bangla/feed.xml"
    # # resp = requests.get(url , headers={
    # #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
    # #
    # # soup = BeautifulSoup(resp.content , features="xml")
    # # entrys = soup.findAll("entry")
    # #
    # # for i in range(10):
    # #     entry = entrys [ i ]
    # #     title = entry.title.text
    # #     summary = entry.summary.text
    # #     ss = entry.link [ 'href' ]
    # #     publish = entry.published.text
    # #     category = entry.category [ 'term' ]
    # #
    # #     if (
    # #             category == "ক্রিকেট" or category == "fun" or category == "বলিউড" or category == "টেলিভিশন" or category == "খেলা" or category == "নিয়োগ" or category == "উচ্চশিক্ষা"
    # #             or category == "টেনিস" or category == "অন্য খেলা" or category == "লাইভ স্কোর" or category == "ফুটবল" or category == "সাক্ষাৎকার"
    # #             or category == "লাইফস্টাইল" or category == "ফ্যাশন" or category == "স্টাইল" or category == "ফুটবল" or category == "রূপচর্চা" or category == "গৃহসজ্জা" or category == "রসনা" or category == "কেনাকাটা"
    # #             or category == "বিনোদন" or category == "ঢালিউড" or category == "আলাপন" or category == "নাটক" or category == "গান" or category == "হলিউড"
    # #             or category == "kishoralo" or category == "golpo" or category == "প্র স্বাস্থ্য"
    # #     ):
    # #         continue
    # #     else:
    # #         result = "Title: " + title + \
    # #                  "\nSummary: " + summary \
    # #                  + "\nLink: " + ss \
    # #                  + "\nPublished: " + publish \
    # #                  + "\nCategory: " + category + "\n"
    # #
    # #         # # print(result)
    # #         # now = datetime.now( )
    # #         #
    # #         # now = datetime.now( )
    # #         #
    # #         # tits = now.strftime("%H:%M:%S")
    # #         #
    # #         # current_time = tits [ 0:5 ]
    # #         # current_date = now.date( )
    # #         #
    # #         # qq = """ INSERT INTO prothomalo (pa_date, pa_published, pa_title , pa_link) VALUES (%s , %s, %s, %s)"""
    # #         # tu = (current_date , publish , title , ss)
    # #         # cursor.execute(qq , tu)
    # #
    # #         print("before insertion")
    # #
    # #         qq = """ INSERT INTO prothomalo (pa_date, pa_time, pa_published, pa_title , pa_link, pa_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
    # #         tu = (current_date , current_time , publish , title , ss , summary)
    # #         cursor.execute(qq , tu)
    # #
    # #         print("Inserted")
    # #
    # #         duplicate_query3 = 'delete from prothomalo b1 using prothomalo b2 where b1.pa_id < b2.pa_id and b1.pa_title = b2.pa_title '
    # #         cursor.execute(duplicate_query3)
    # #         print("Removed duplicates")
    # #
    # #     # # ##### fetch from database
    # # postgreSQL_select_Query = ("select * from prothomalo where pa_time= '%s'" % current_time)
    # #
    # # cursor.execute(postgreSQL_select_Query)
    # # # print ( "Selecting rows from mobile table using cursor.fetchall" )
    # # mobile_records = cursor.fetchall( )
    # #
    # # print("Messages  prothomalo are being send")
    # # for row in mobile_records:
    # #     # print ( "Id = " , row [ 0 ] , )
    # #     # print ( "Date = " , row [ 1 ] )
    # #     # print ( "Time  = " , row [ 2 ]  )
    # #     # print ( "Published = " , row [ 3 ] )
    # #     # print ( "Title  = " , row [ 4 ]  )
    # #     # print ("Link = ", row[ 5 ], "\n")
    # #
    # #     message = "Link: " + row [ 5 ] + \
    # #               "\nPublished: " + row [ 3 ] \
    # #               + "\nTitle: " + row [ 4 ] \
    # #               + "\nSummary: " + row [ 6 ] \
    # #               + "\n"
    # #     sleep(10)
    # #     print('This is your message..')
    # #     print(message)
    # #     message = quote(message)
    # #     numbers = [ ]
    # #     f = open("numbers.txt" , "r")
    # #     for line in f.read( ).splitlines( ):
    # #         if line != "":
    # #             numbers.append(line)
    # #     f.close( )
    # #     total_number = len(numbers)
    # #
    # #     print('\nWe found ' + str(total_number) + ' numbers in the file')
    # #
    # #     print( )
    # #     delay = 30
    # #
    # #     # if platform == "win32":
    # #     #
    # #     # else:
    # #     #     driver = webdriver.Chrome ( "./drivers/chromedriver" , options=options )
    # #     print('Once your browser opens up sign in to web whatsapp')
    # #     sleep(20)
    # #     # input ( "Press ENTER after login into Whatsapp Web and your chats are visiable	." )
    # #     for idx , number in enumerate(numbers):
    # #         if number == "":
    # #             continue
    # #         print('{}/{} => Sending message to {}.'.format((idx + 1) , total_number , number))
    # #         try:
    # #             url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
    # #             driver.get(url)
    # #             try:
    # #                 click_btn = WebDriverWait(driver , delay).until(
    # #                     EC.element_to_be_clickable((By.CLASS_NAME , '_2Ujuu')))
    # #             except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
    # #                 print("alert present")
    # #                 Alert(driver).accept( )
    # #             sleep(1)
    # #             click_btn.click( )
    # #             sleep(3)
    # #             print('Message sent to: ' + number)
    # #         except Exception as e:
    # #             print('Failed to send message to ' + number + str(e))
    # #
    # # # newspapers = [ 'thedailystar' ]
    # # #
    # # # #### newspaper iteration
    # # # for newspaper in newspapers:
    # # #     article_list = read_content.get('newspapers').get(newspaper).get('articles')
    # # #     for i in article_list:
    # # #         values = i.values( )
    # # #         values_list = list(values)
    # # #         listToStr = '~~'.join(map(str , values_list))
    # # #         # print(listToStr,'\n')
    # # #         l = listToStr.split('~~')
    # # #
    # # #         result = "Link: " + l [ 0 ] + \
    # # #                  "\nPublished: " + l [ 1 ] \
    # # #                  + "\nTitle: " + l [ 2 ] \
    # # #                  + "\nSummary: " + l [ 3 ] + "\n"
    # # #
    # # #         dt = l [ 2 ]
    # # #         dl = l [ 0 ]
    # # #         dp = l [ 1 ]
    # # #         ds = l [ 3 ]
    # # #         # current_time = now.strftime("%H:%M:%S")
    # # #         # current_date = now.date()
    # # #
    # # #         # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
    # # #         # tu = (current_date, dp, dt, dl)
    # # #         # cursor.execute(qq,tu)
    # # #         print("before insertion")
    # # #
    # # #         qq = """ INSERT INTO dailystar (ds_date, ds_time, ds_published, ds_title , ds_link, ds_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
    # # #         tu = (current_date , current_time , dp , dt , dl , ds)
    # # #         cursor.execute(qq , tu)
    # # #
    # # #         print("Inserted")
    # # #
    # # #         duplicate_query3 = 'delete from dailystar b1 using dailystar b2 where b1.ds_id < b2.ds_id and b1.ds_title = b2.ds_title '
    # # #         cursor.execute(duplicate_query3)
    # # #         print("Removed duplicates")



    connection.commit( )


except (Exception , psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL" , error)

finally:
    # closing database connection.
    if (connection):
        cursor.close ( )
        connection.close ( )
        print ( "PostgreSQL connection is closed" )