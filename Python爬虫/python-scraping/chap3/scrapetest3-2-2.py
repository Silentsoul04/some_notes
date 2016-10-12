from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.ichenfei.com/archive")
bsObj = BeautifulSoup(html.read(),"html.parser")

items = bsObj.find("article").find_all("a")

# print(items)
for item in items:
    print(item.attrs["href"]+item.get_text())