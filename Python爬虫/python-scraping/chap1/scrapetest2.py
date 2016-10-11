#!/usr/bin/python3
"""
BeautifulSoup 是一个可以从HTML或XML文件中提取数据的Python库.
它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.html)

