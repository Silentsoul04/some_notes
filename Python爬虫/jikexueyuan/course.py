#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

class JikeSpider(object):
    def __init__(self):
        print u"开始爬取内容。。。"

    def getSource(self,url):
        html = requests.get(url,headers = headers)
        return html.text

    def changePage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for pageNum in range(now_page,total_page+1):
            link = re.sub('pageNum=(\d+)','pageNum=%s' % pageNum,url,re.S)
            page_group.append(link)
        return page_group

    def getEveryClass(self,source):
        every_class = re.findall('<li(.*?)</li>',source,re.S)
        return every_class

jikespider = JikeSpider()

print jikespider.changePage("http://www.jikexueyuan.com/course/?pageNum=1",20)