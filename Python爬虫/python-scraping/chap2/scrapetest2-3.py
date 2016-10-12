from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"

html = urlopen(url)
bsObj = BeautifulSoup(html.read(),"html.parser")

# print(bsObj)

print(bsObj.find_all("img"))
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)
