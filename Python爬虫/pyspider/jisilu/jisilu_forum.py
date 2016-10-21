#-*- coding:utf8 -*-

import requests
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

url = "https://www.jisilu.cn/home/explore/sort_type-new__day-0__page-1"
html = requests.get(url,headers=headers).content

print html
