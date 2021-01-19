# from tkinter import *
# import json
#
# with open ('scraped_english_articles.json') as access_json:
#     read_content = json.load (access_json)
#
# # print(read_content)
# # print(type(read_content))
#
# list = list(read_content.items())
# # print(list)
#
# listToStr = '~~'.join (map (str , list))
# l= listToStr.split('~~')
# print(l)

# import tkinter as tk
# import json
#
# app = tk.Tk()
#
# text = tk.Text(app)
#
# text.pack()
#
# with open ('scraped_english_articles.json') as access_json:
#     read_content = json.load (access_json)
#
# # json_val = json.loads('{"a": 5, "b": 7}')
#
# for k in read_content:
#     text.insert(tk.END, '{} = {}\n'.format(k,read_content[k]))
# text.config(state = tk.DISABLED)
# app.mainloop()

import os
from tkinter import *
from subprocess import Popen, PIPE
root = Tk()
text = Text(root)
text.pack()

def ls_proc():
    return Popen(['ls'], stdout=PIPE)

with ls_proc() as p:
    if p.stdout:
        for line in p.stdout:
            text.insert(END, line)
    if p.stderr:
        for line in p.stderr:
            text.insert(END, line)

root.mainloop()