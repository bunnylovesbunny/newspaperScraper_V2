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




for i in range(20):
    entry = entrys[i]
    title = entry.title.text
    summary = entry.summary.text
    ss = entry.link [ 'href' ]
    publish = entry.published.text
    category = entry.category ['term']


    if(category=="ক্রিকেট" or category=="fun" or category=="বলিউড" or category=="টেলিভিশন" or category=="খেলা" or category=="নিয়োগ" or category=="উচ্চশিক্ষা"
    or category=="টেনিস" or category=="অন্য খেলা" or category=="লাইভ স্কোর" or category=="ফুটবল" or category=="সাক্ষাৎকার"
    or category == "লাইফস্টাইল" or category == "ফ্যাশন" or category == "স্টাইল" or category == "ফুটবল" or category == "রূপচর্চা" or category=="গৃহসজ্জা" or category=="রসনা" or category== "কেনাকাটা"
    or category=="বিনোদন" or category=="ঢালিউড" or category=="আলাপন" or category=="নাটক" or category=="গান" or category=="হলিউড"
    or category == "kishoralo" or category == "golpo" or category == "প্র স্বাস্থ্য"
    ):
        continue
    else:
        result = "Title: " + title + \
                 "\nSummary: " + summary \
                 + "\nLink: " + ss \
                 + "\nPublished: " + publish \
                 + "\nCategory: " + category + "\n"

        print (category)
        # print(result)
        now = datetime.now ()

        current_time = now.strftime ("%H:%M:%S")
        l = current_time.split (':')

        current_hour = l [ 0 ]
        current_min = l [ 1 ]

    # print ("Your message will be deliverd @ " , current_hour , " : " , int (current_min) + 3)
    # print ( result )

    #pywhatkit.sendwhatmsg ( '+8801866690414' , result , int ( current_hour ) , (int ( current_min ) + 3) )
   # pywhatkit.sendwhatmsg_to_group('Kamla V-2' , result , int ( current_hour ) , (int ( current_min ) + 3))






