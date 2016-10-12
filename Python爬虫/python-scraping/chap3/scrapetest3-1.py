from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(),"html.parser")

items = bsObj.find_all("a")


##查找http://en.wikipedia.org/wiki/Kevin_Bacon 页面的链接
for item in items:
    if "href" in item.attrs:
        print(item.attrs["href"])
    # print(item)