from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,"html.parser")

"""
wikipedia 指向词条的链接有三个特点:

它们都有三个共同点：
• 它们都在 id 是 bodyContent 的 div 标签里
• URL 链接不包含冒号
• URL 链接都以 /wiki/ 开头

"""
items = bsObj.find("div",id="bodyContent").find_all("a",{"href":re.compile("^(/wiki)((?!:).)*$")})

# print(items)
for item in items:
    print(item.attrs["href"])