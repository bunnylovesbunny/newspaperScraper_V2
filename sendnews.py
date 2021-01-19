import pywhatkit
import requests
from bs4 import BeautifulSoup
import urllib3
import re
from datetime import datetime
import time
import pywhatkit
import json
from tkinter import *

root = Tk()


# Opening JSON file
# with open('scraped_english_articles.json') as access_json:
#     read_content = json.load(access_json)
#
#
# newspapers = ['bbc', 'thedailystar','banglatribune']
#
# article_list = []




# def sendnews():
#     with open ('scraped_english_articles.json') as access_json:
#         read_content = json.load (access_json)
#
#     article_list = []
#     newspapers = [ 'bbc' , 'thedailystar' , 'banglatribune' ]
#     for newspaper in newspapers:
#         article_list = read_content.get ('newspapers').get (newspaper).get ('articles')
#
#
#     for i in article_list:
#         print(i)
#
#
#     result = [ ]
#
#     for i in article_list:
#         values = i.values ()
#         values_list = list ( values )
#         listToStr = '\n\n'.join ( map ( str , values_list ) )
#         result.append ( listToStr )
#         # for item in result:
#         now = datetime.now ()
#         current_time = now.strftime ( "%H:%M:%S" )
#         l = current_time.split ( ':' )
#
#         current_hour = l [ 0 ]
#         current_min = l [ 1 ]
#         print ( "Your message will be deliverd @ " , current_hour , " : " , int ( current_min ) + 3 )
#         # pywhatkit.sendwhatmsg ( "+8801866690414" , listToStr , int ( current_hour ) , (int ( current_min ) + 3) )
#
#         # print ( "going to sleep for " , (1.1 * 60) , " sec\n" )
#         # time.sleep ( 1.1 * 60 )
#
#
# # for newspaper in newspapers:
# #     article_list = read_content.get('newspapers').get(newspaper).get('articles')
# #     sendnews()

phone_number = ["+8801866690414","+8801777701716"]


def sendnews():
    with open ('scraped_english_articles.json') as access_json:
        read_content = json.load (access_json)


    newspapers = [ 'bbc' , 'thedailystar']
    for newspaper in newspapers:
        article_list = read_content.get ('newspapers').get (newspaper).get ('articles')
        for i in article_list:
            values = i.values()
            values_list = list (values)
            listToStr = '~~'.join (map (str , values_list))
            # print(listToStr,'\n')
            l= listToStr.split('~~')

            result = "Link: " + l[0] + \
                     "\nPublished: " + l[1] \
                     + "\nTitle: " + l[2] \
                     + "\nSummary: " + l[3] + "\n"
            now = datetime.now ()
            current_time = now.strftime ("%H:%M:%S")
            l = current_time.split (':')
            current_hour = l [ 0 ]
            current_min = l [ 1 ]
            print ("Your message will be deliverd  " , current_hour , " : " , int (current_min) + 3)
            print(l[2])

            label =Label(root, text = "Deliver at" + current_hour + ":" + current_min,
                         relief = RAISED )
            label.pack()


            # print ("Your message will be deliverd @ " , current_hour , " : " , int (current_min) + 3)
            #
            # print(result)

            # myLabel01= Label (root,text= "Your message will be deliverd @ "+ current_hour + ":" + str(int(current_min)+3)  )
            # myLabel01.pack()
            #
            # myLabel02 = Label (root ,text=result)
            # myLabel02.pack ()
            # root.mainloop ()
            pywhatkit.sendwhatmsg ('+8801866690414' , result , int (current_hour) , int (current_min) + 3)





            # for i in phone_number:
            #     pywhatkit.sendwhatmsg(i,result, int(current_hour),int(current_min)+3)

sendnews()
root.mainloop()
