#-*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

def getDateTime(title):
    try:
        date = re.search(r'.*(201[1-6][0-9][0-9][0-9][0-9]).*', title).group(1)
    except AttributeError as e:
        date = None
    return date

def getLinJie(url):
    rep = requests.get(url).content
    try:
        szlj = re.search('上证(继续|转)(.*?)临界(\d+)',rep).group(0)
    except AttributeError as e:
        szlj = "0000"
    return szlj

url = "https://www.gushequ.cc/archives"

response = requests.get(url).content
bsObj = BeautifulSoup(response,"html.parser")
archive_links =  bsObj.find("article").find_all("a")
for archive_link in archive_links:
    archive_url = archive_link.attrs["href"]
    title = archive_link.get_text()
    datetime = getDateTime(title)
    if datetime:
        print datetime + ":"
        print getLinJie(archive_url)