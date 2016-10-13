from urllib.request import urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup
import re
"""
递归收集wikipedia的链接
"""

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    links = bsObj.find_all("a",{"href":re.compile("^(/wiki)((?!:).)*$")})
    for link in links:
        if("href" in link.attrs):
            #找到新页面
            if(link.attrs["href"] not in pages):
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
        else:
            continue




# print(items)
getLinks("/wiki/Python")