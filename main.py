from tkinter import *
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

root = Tk()

news_url="https://prod-qt-images.s3.amazonaws.com/production/prothomalo-bangla/feed.xml"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("entry")
# Print news title, url and publish date
for news in news_list:
    myLabel01 = Label (root , text=news.title.text)
    myLabel01.pack ()
    myLabel02 = Label (root , text=news.summary.txt)
    myLabel02.pack ()
    myLabel03 = Label (root , text=news.link['href'])
    myLabel03.pack ()
    myLabel04 = Label (root , text=news.published.text)
    myLabel04.pack ()
    myLabel05 = Label (root , text="-"*60)
    myLabel05.pack ()
    root.mainloop ()
  # myLabel01= Label (root,text= "Your message will be deliverd @ "+ current_hour + ":" + str(int(current_min)+3)  )



  # print(news.title.text)
  # print(news.summary.text)
  # print(news.link['href'])
  # print(news.published.text)
  #
  # print("-"*60)


  # title = entry.title.text
  # summary = entry.summary.text
  # ss = entry.link [ 'href' ]
  # publish = entry.published.text
