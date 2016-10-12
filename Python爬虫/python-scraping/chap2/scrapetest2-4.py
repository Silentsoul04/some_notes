from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = urlopen("http://www.pythonscraping.com/pages/page3.html")

html = url.read()

bsObj = BeautifulSoup(html,"html.parser")

print(bsObj.body.find_all(lambda tag:len(tag.attrs)==2))