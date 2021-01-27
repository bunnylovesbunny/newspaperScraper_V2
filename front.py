from tkinter import *
import back
import sys
import os
import subprocess as sub

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,selected_tuple[3])
    # entry4.delete(0,END)
    # entry4.insert(END,selected_tuple[4])
    # entry5.delete(0,END)
    # entry5.insert(END,selected_tuple[5])
    entry4.delete(0,END)
    entry4.insert(END,selected_tuple[4])

def view_command_bbc():
    list1.delete(0,END)
    for row in back.viewbbc():
        list1.insert(END,row)

def view_command_prothomalo():
    list1.delete(0,END)
    for row in back.viewprothomalo():
        list1.insert(END,row)

def view_command_dailystar():
    list1.delete(0,END)
    for row in back.viewdailystar():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back.search(published_text.get(),date_text.get(),title_text.get(),link_text.get()):
        list1.insert(END,row)

def collect_command():
    # back.insert(published_text.get(),date_text.get(),title_text.get(),link_text.get())
    list1.delete(0,END)
    list1.insert(END, 'News with RSS Feed link is being downloaded')

    for i in range (4):
        list1.insert(END,"Downloading...")

    os.system('python newsscraper.py')
    list1.insert(END, 'Download Complete')


def delete_command():
    back.delete(selected_tuple[0])

def update_command():
    back.update(selected_tuple[0],published_text.get(),date_text.get(),title_text.get(),link_text.get())

def send_command():
    list1.delete(0,END)
    os.system('python testDB.py')
    list1.delete(0, END)
    list1.insert(END, 'News are send to')
    for row in back.sendlist():
        list1.insert(END, row)


window=Tk()
window.title("Panda Project")
window.geometry('800x500')
window.configure(bg = 'bisque')

label1=Label(window,text="",width=15,bg = 'bisque')
label1.grid(row=0,column=2)

label2=Label(window,text="DATE",width=15,bg = 'bisque',padx=30)
label2.grid(row=1,column=0)

label3=Label(window,text="TIME",width=15,bg = 'bisque')
label3.grid(row=2,column=0)

label4=Label(window,text="PUBLISHED",width=15,bg = 'bisque')
label4.grid(row=3,column=0)

# label5=Label(window,text="number of days you want to stay in:")
# label5.grid(row=4,column=0)
#
# label6=Label(window,text="Room type(Normal , king or delux) :")
# label6.grid(row=5,column=0)

label7=Label(window,text="TITLE",width=15,bg = 'bisque')
label7.grid(row=4,column=0)

published_text=StringVar()
entry1=Entry(window,textvariable=published_text)
entry1.grid(row=1,column=1)

date_text=StringVar()
entry2=Entry(window,textvariable=date_text)
entry2.grid(row=2,column=1)

title_text=StringVar()
entry3=Entry(window,textvariable=title_text)
entry3.grid(row=3,column=1)

link_text=StringVar()
entry4=Entry(window,textvariable=link_text)
entry4.grid(row=4,column=1)
#
# roomtype_text=StringVar()
# entry5=Entry(window,textvariable=roomtype_text)
# entry5.grid(row=5,column=1)

link_text=StringVar()
entry6=Entry(window,textvariable=link_text)
entry6.grid(row=4,column=1)

list1=Listbox(window,height=20,width=59)
list1.grid(row=1,column=3, rowspan=10, columnspan=5)

scrly=Scrollbar(window)
scrly.grid(row=1,column=2, sticky='ns',rowspan=10)

list1.configure(yscrollcommand=scrly.set)
scrly.configure(command=list1.yview)


# scrlx=Scrollbar(window)
# scrlx.grid(row=11,column=3, sticky='ns',columnspan=2)
#
# list1.configure(xscrollcommand=scrlx.set)
# scrlx.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="Collect News",width=15, command=collect_command)
b1.grid(row=7, column=1)

b2=Button(window,text="View BBC",width=15,command=view_command_bbc)
b2.grid(row=8, column=0)

b3=Button(window,text="View Prothomalo",width=15,command=view_command_prothomalo)
b3.grid(row=9, column=0)

b4=Button(window,text="View DailyStar",width=15,command=view_command_dailystar)
b4.grid(row=7, column=0)

b5=Button(window,text="Send News",width=15,command=send_command)
b5.grid(row=8, column=1)

b6=Button(window,text="Search",width=15,command=search_command)
b6.grid(row=9, column=1)


window.mainloop()