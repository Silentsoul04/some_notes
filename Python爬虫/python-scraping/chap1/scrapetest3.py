#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    # 异常发生时，程序会返回 HTTP 错误。HTTP 错误可能是404 500等。
    try:
        html = urlopen(url)
    except HTTPError as e:
        #print(e)
        return None
        # 返回空值，中断程序，或者执行另一个方案
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.find_all("html")
    except AttributeError as e:
        #print(e)
        return None
    return title

html = "http://pythonscraping.com/pages/page1.html"
title = getTitle(html)
if(title==None):
    print("Title does not exist")
else:
    print(title)