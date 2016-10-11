#!/usr/bin/python3

"""
urllib与urllib2:
Python 3.x 里，urllib2 改名为 urllib，被分成一些子模块： urllib.request、urllib.parse 和 urllib.error 。
尽管函数名称大多和原来一样，但是在用新的 urllib 库时需要注意哪些函数被移动到子模块里了。

urlopen 用来打开并读取一个从网络获取的远程对象。因为它是一个非常通用的库（它可以轻松读取 HTML 文件、图像文件，或其他任何文件流），
所以我们将在本书中频繁地使用它。
"""

from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")

print(html.read())

