from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from urllib.error import URLError
import pymysql
import datetime
import random
import re


conn = pymysql.connect(host='182.254.226.241',user='hhf',passwd='hhf960214',db='scraping',charset="utf8")
cur = conn.cursor()
# cur.execute("desc pages;")
random.seed(datetime.datetime.now())

urlList = set()

def store(title,content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
    cur.connection.commit()

def get_Links(articleUrl):
    try:
        html = urlopen("https://en.wikipedia.org" + articleUrl)
    except URLError as e:
        print(e)
        return None
    bsObj = BeautifulSoup(html,"html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    links = bsObj.find("div",{"id":"content"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    for link in links:
        urlList.add(link)
    return links

links = get_Links("/wiki/Python")

try:
    while(len(links)>=0):
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links = get_Links(newArticle)

finally:
    cur.close()
    conn.close()