from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

urlbase = "http://www.pythonscraping.com/"

htmlurl = urlbase + "pages/page3.html"

html = urlopen(htmlurl)
bsObj = BeautifulSoup(html.read(),"html.parser")

# print(bsObj)

imgs = bsObj.find_all("img",{"src":re.compile("\.\.\/img\/gifts/img(.*)\.jpg")})

for img in imgs:
    print(img["src"])  #属性参数 attributes 是用一个 Python字典封装一个标签的若干属性和对应的属性值。