import requests
from bs4 import BeautifulSoup
import urllib3
import re
from datetime import datetime
import time

import pywhatkit


url = "https://prod-qt-images.s3.amazonaws.com/production/prothomalo-bangla/feed.xml"
resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

soup = BeautifulSoup(resp.content, features="xml")
entrys = soup.findAll("entry")

data = {}
data["newspapers"] = {}



# entry = entrys[0]
# title = entry.title.text
# summary= entry.summary.text
#
# links = soup.findAll("link")
# ss= entry.link['href']
#
#
#
#
# result = "Title: "+title +"\nSummary: " + summary+ "\nLink: " + ss +"\n"
#
# print(result)
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# l = current_time.split(':')
#print(l)
#current_hour = l[0]
#current_min = l[1]
#print(current_hour)
#print(current_min)
#print("Current Time =", current_time)
#print(int(current_min)+4)


#pywhatkit.sendwhatmsg('+8801866690414',result,int(current_hour),(int(current_min)+3))
#pywhatkit.sendwhatmsg_to_group('Kamla V-2',result,16,55)



# def update():
#     while True:
#
#
#
#         entry = entrys[0]
#
#
#         title = entry.title.text
#         summary = entry.summary.text
#
#         links = soup.findAll("link")
#         ss = entry.link['href']
#
#         result = "Title: " + title + "\nSummary: " + summary + "\nLink: " + ss + "\n"
#
#         # print(result)
#
#         now = datetime.now()
#
#         current_time = now.strftime("%H:%M:%S")
#         l = current_time.split(':')
#         # print(l)
#         current_hour = l[0]
#         current_min = l[1]
#          # print(current_hour)
#          # print(current_min)
#          # print("Current Time =", current_time)
#          # print(int(current_min) + 1)
#
#         print(int(current_min)+3)
#         print(result)
#
#         pywhatkit.sendwhatmsg('+8801777701716', result, int(current_hour), (int(current_min) + 3))
#         time.sleep(5 * 60)
#
#
#
# update()

#
# def news():
#     previousString = 'null'
#     while True:
#         entry = entrys[0]
#         m = entry.title.text
#         if(m!=previousString):
#             title = entry.title.text
#             summary = entry.summary.text
#
#             links = soup.findAll("link")
#             ss = entry.link['href']
#
#             result = "Title: " + title + "\nSummary: " + summary + "\nLink: " + ss + "\n"
#
#             # print(result)
#
#             now = datetime.now()
#
#             current_time = now.strftime("%H:%M:%S")
#             l = current_time.split(':')
#             # print(l)
#             current_hour = l[0]
#             current_min = l[1]
#             # print(current_hour)
#             # print(current_min)
#             # print("Current Time =", current_time)
#             # print(int(current_min) + 1)
#
#             print(int(current_min) + 3)
#             print(result)
#
#             pywhatkit.sendwhatmsg('+8801866690414', result, int(current_hour), (int(current_min) + 3))
#             previousString=m
#             print(previousString)
#             time.sleep(5 * 60)
#
#         else:
#             time.sleep(5 * 60)
#
# news()


for i in range(1):
    entry = entrys[i]
    title = entry.title.text
    summary = entry.summary.text
    ss = entry.link [ 'href' ]
    publish = entry.published.text



    result = "Title: " + title + \
             "\nSummary: " + summary \
             + "\nLink: " + ss \
             + "\nPublished: "+ publish + "\n"

    print(result)
    now = datetime.now ()

    current_time = now.strftime ( "%H:%M:%S" )
    l = current_time.split ( ':' )

    current_hour = l [ 0 ]
    current_min = l [ 1 ]

    print ("Your message will be deliverd @ " , current_hour , " : " , int (current_min) + 3)
    print ( result )

    pywhatkit.sendwhatmsg ( '+8801866690414' , result , int ( current_hour ) , (int ( current_min ) + 3) )
   # pywhatkit.sendwhatmsg_to_group('Kamla V-2' , result , int ( current_hour ) , (int ( current_min ) + 3))





# def sendNews():
#     entry = entrys[0]
#     m = entry.title.text
#     previousNews = 'null'
#     if (m == previousNews):
#         flag=0
#     else:
#         title = entry.title.text
#         summary = entry.summary.text
#         ss = entry.link['href']
#         category = entry.link['term']
#         result = "Title: " + title + \
#                  "\nSummary: " + summary \
#                  + "\nLink: " + ss \
#                  + "\nCategory: " + category
#
#
#
#         now = datetime.now()
#
#         current_time = now.strftime("%H:%M:%S")
#         l = current_time.split(':')
#
#         current_hour = l[0]
#         current_min = l[1]
#
#
#         print(int(current_min) + 3)
#         print(result)
#
#         pywhatkit.sendwhatmsg('+8801866690414', result, int(current_hour), (int(current_min) + 3))
#         previousNews = m
#         flag=1
#         print(previousNews)
#
#
# def executeNews():
#     while True:
#         if(flag==1):
#             sendNews()
#             time.sleep(5*60)
#
#         elif (flag==0):
#             time.sleep(5*60)
#
# executeNews()
