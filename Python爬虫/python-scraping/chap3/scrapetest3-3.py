from urllib.request import urlopen
# from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html.read(),"html.parser")
    links = bsObj.find("div",id="bodyContent").find_all("a",{"href":re.compile("^(/wiki)((?!:).)*$")})
    return links

links = getLinks("/wiki/Python")

# print(items)
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)