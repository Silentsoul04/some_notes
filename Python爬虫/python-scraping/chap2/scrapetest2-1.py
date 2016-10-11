from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(),"html.parser")

# print(bsObj)

#find_all(tag, attributes, recursive, text, limit, keywords)

###查找属性 attributes
green_text = bsObj.find_all("span", {"class":{"green", "red"}})
print(green_text)

###查找内容 text
nameList = bsObj.find_all(text="the prince")
print(len(nameList))

###查找关键词 keyword
allText = bsObj.find_all(id="text")
print(allText[0].get_text())