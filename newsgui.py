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
from tkinter import *
from subprocess import Popen, PIPE
root = Tk()
txt = Text (root, width =30, height=20, wrap = WORD )
txt.pack()
try:

    txt.delete(0.0,'end')
    options = Options ( )
    driver = webdriver.Chrome("drivers\\chromedriver.exe" , options=options)
    driver.get('https://web.whatsapp.com')

    connection = psycopg2.connect ( user="postgres" ,
                                    password="123456" ,
                                    host="127.0.0.1" ,
                                    port="5432" ,
                                    database="postgres" )
    cursor = connection.cursor ( )

    ##### fetch data from json file
    with open ('scraped_english_articles.json') as access_json:
        read_content = json.load (access_json)
    txt.insert(0.0, "Feteching News Articles")
    now = datetime.now ( )
    tits = now.strftime ( "%H:%M:%S" )

    current_time = tits [ 0:5 ]
    current_date = now.date ( )

    #------------------------------------------- task for daily star ---------------------------------------------------------#

    newspapers = ['thedailystar']

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
            # current_time = now.strftime("%H:%M:%S")
            # current_date = now.date()


            # qq = """ INSERT INTO dailystar (ds_date, ds_published, ds_title , ds_link) VALUES (%s , %s, %s, %s)"""
            # tu = (current_date, dp, dt, dl)
            # cursor.execute(qq,tu)
            # print("before insertion")
            txt.insert(0.0 , "before insertion")

            qq = """ INSERT INTO dailystar (ds_date, ds_time, ds_published, ds_title , ds_link, ds_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
            tu = (current_date , current_time, dp , dt , dl,ds)
            cursor.execute ( qq , tu )

            qq = """ INSERT INTO senddailystar (sendds_date, sendds_time, sendds_published, sendds_title , sendds_link, sendds_summary) VALUES (%s ,%s, %s, %s, %s, %s)"""
            tu = (current_date , current_time , dp , dt , dl , ds)
            cursor.execute(qq , tu)

            # print("Inserted")
            txt.insert(0.0 , "inserted")
            duplicate_query3 = 'delete from dailystar b1 using dailystar b2 where b1.ds_id < b2.ds_id and b1.ds_title = b2.ds_title '
            cursor.execute ( duplicate_query3 )
            # print ("Removed duplicates")
            txt.insert(0.0 , "Removed duplicates")

    # # ##### fetch from database
    postgreSQL_select_Query = ("select * from dailystar where ds_time= '%s'" %current_time)

    cursor.execute ( postgreSQL_select_Query)
    # print ( "Selecting rows from mobile table using cursor.fetchall" )
    mobile_records = cursor.fetchall ( )



    # print ( "Messages daily star are being send" )

    for row in mobile_records:
        # print ( "Id = " , row [ 0 ] , )
        # print ( "Date = " , row [ 1 ] )
        # print ( "Time  = " , row [ 2 ]  )
        # print ( "Published = " , row [ 3 ] )
        # print ( "Title  = " , row [ 4 ]  )
        # print ("Link = ", row[ 5 ], "\n")

        message = "Link: " + row [ 5 ] + \
                  "\nPublished: " + row [ 3 ] \
                  + "\nTitle: " + row [ 4 ] \
                  + "\nSummary: " + row [6] \
                  + "\n"
        sleep(10)
        # print ( 'This is your message..' )
        # print ( message )
        txt.insert(0.0 , message)
        message = quote ( message )
        numbers = [ ]
        f = open ( "numbers.txt" , "r" )
        for line in f.read ( ).splitlines ( ):
            if line != "":
                numbers.append ( line )
        f.close ( )
        total_number = len ( numbers )

        # print ( '\nWe found ' + str ( total_number ) + ' numbers in the file' )
        m= '\nWe found ' + str ( total_number ) + ' numbers in the file'
        txt.insert(0.0 , m)
        # delete_news = ("delete from dailystar where ds_title= '%s'" % row[4])
        # cursor.execute(delete_news)
        print ( )
        delay = 30

        # if platform == "win32":
        #
        # else:
        #     driver = webdriver.Chrome ( "./drivers/chromedriver" , options=options )
        # print ( 'Once your browser opens up sign in to web whatsapp' )
        sleep ( 20 )
        # input ( "Press ENTER after login into Whatsapp Web and your chats are visiable	." )
        for idx , number in enumerate ( numbers ):
            if number == "":
                continue
            # print ( '{}/{} => Sending message to {}.'.format ( (idx + 1) , total_number , number ) )
            m2= '{}/{} => Sending message to {}.'.format ( (idx + 1) , total_number , number)
            txt.insert(0.0, m2)
            try:
                url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
                driver.get ( url )
                try:
                    click_btn = WebDriverWait ( driver , delay ).until (
                        EC.element_to_be_clickable ( (By.CLASS_NAME , '_2Ujuu') ) )
                except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
                    # print ( "alert present" )
                    Alert ( driver ).accept ( )
                sleep ( 1 )
                click_btn.click ( )
                sleep ( 3 )
                # print ( 'Message sent to: ' + number )
            except Exception as e:
                # print ( 'Failed to send message to ' + number + str ( e ))
                m3 = 'Failed to send message to ' + number + str ( e )
                txt.insert(0.0 , m3)

    connection.commit()

finally:
    # closing database connection.
    if (connection):
        cursor.close ( )
        connection.close ( )
        # print ( "PostgreSQL connection is closed" )


root.mainloop()