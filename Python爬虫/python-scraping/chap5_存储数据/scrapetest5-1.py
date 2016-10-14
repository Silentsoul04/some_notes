from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/"
html = urlopen(url)
bsObj = BeautifulSoup(html,"html.parser")

imgLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imgLocation,"test/logo.jpg")