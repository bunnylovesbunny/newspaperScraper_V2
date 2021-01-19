import sys
import os
from tkinter import *


window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run(args):
    if args == 1:

        os.system('python newsscraper.py')
        # my_label1.config(text="Downloading News")

    if args == 2:

        os.system('python sendnewsV2.py')
        # my_label2.config(text="Sending News on Whatsapp")

    if args == 3:

        os.system('python database01.py')
        # my_label3.config(text="Storing News in Database")

    if args == 4:

        os.system('python database02.py')
        # my_label3.config(text="Storing News in Database")

    if args == 5:
        os.system(exit())




btn1 = Button(window, text="Collect News", bg="black", fg="white",command=lambda:run(1))
btn2 = Button(window, text="Send News", bg="black", fg="white",command=lambda:run(2))
btn3 = Button(window, text="Insert News", bg="black", fg="white",command=lambda:run(3))
btn4 = Button(window, text="Remove Duplicates", bg="black", fg="white",command=lambda:run(4))
btn5 = Button(window, text="Exit System", bg="black", fg="white",command=lambda:run(5))


btn1.grid(column=1, row=0,padx=10, pady=10)
btn2.grid(column=2, row=0,padx=10, pady=10)
btn3.grid(column=3, row=0,padx=10, pady=10)
btn4.grid(column=4, row=0,padx=10, pady=10)
btn5.grid(column=5, row=0,padx=10, pady=10)
# global my_label1,my_label2,my_label3
# my_label1 = Label(window, text = "WhatsAppBot", command = lambda:run(1))
# my_label1.pack(pady=10)
# my_label2 = Label(window, text = "WhatsAppBot", command = lambda:run(2))
# my_label2.pack(pady=10)
# my_label3 = Label(window, text = "WhatsAppBot",command = lambda:run(3))
# my_label3.pack(pady=10)
window.mainloop()