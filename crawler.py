# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

import requests

def getHtml():
    postsAndLinks = list()
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    url = 'https://toutiao.io/'
    html = requests.get(url, headers=hd).text  # get source code
    soup = BeautifulSoup(html, "html.parser")
    todayPosts = soup.find_all('div', class_='post')
    for todayPost in todayPosts:
        postSoup = BeautifulSoup(str(todayPost), "html.parser")
        postsAndLinks.append([postSoup.find(name='a', attrs={'rel': 'external'}).contents[0],
                              postSoup.find(name='a', attrs={'rel': 'external'})['href']])
    return postsAndLinks


for record in getHtml():
    print 'title:' + record[0] + ' link:https://toutiao.io' + record[1]
