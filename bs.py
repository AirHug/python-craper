# -*- coding:utf-8 -*-
from Tkinter import *
from ScrolledText import ScrolledText 
# urllib,urllib2,re,requests,beautifulsoup 4

import urllib, requests
import re 
import threading
#catch imformation from web page
#url->resource code->get video or some files->download and show the data
#aim web: www.budejie.com/video/

url_name = []# url+name
pageNum = 1

def get():
    global pageNum
    hd = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    url = 'http://www.budejie.com/video/' + str(pageNum)
    varl.set('we have get the %s'%(pageNum))
    html = requests.get(url, headers=hd).text#get source code
    #print html
    a+=1
    url_content = re.compile(r'<div class="j-r-list-c">.*?</div>.*?</div>', re.S)
    url_contents = re.findall(url_content, html)
    # 中文在可迭代对象就是 unicode
    print url_contents
    for i in url_contents
        url_reg = r'data-,p4="(.*?)">'
        url_items = re.findall(url_reg, i)
        print url_items    
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}.html?"')
            name_items = re.findall(name_reg, i)
            for i, k in zip(name_items, url_items):
                url_name.append([i,k])
                print i, k
    return url_name

id = 1#vedio

def write():
    global id
    while id<10:
        url_name = get()
        for i in url_name
            urllib.urlretrieve(i[1], 'video\\%s.mp4' % (i[0].decode('utf-8').encode('gbk')))
            text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            url_name.pop(0)
            id+=1
    varl.set('over!')

def start():
    th = threading.Thread(target=write)
    th.start()#触发

root = Tk() #create a instance
root.title('my first python window')
root.geometry('600x300')# size
root.geometry('+100+200')# position
root.geometry('600x300+100+200')# compact
text = ScrolledText(root, font=('微软雅黑',10))
text.grid() # layout

button = Button(root, text='start crap', font=('微软雅黑', 10), command = start)
button.grid()

varl = StringVar()
label = Label(root, font=('微软雅黑', 10), fg='red', testvariable = varl)
label.grid()
varl.set('I am ready!')


root.mainloop() # create window and get into information loop.
