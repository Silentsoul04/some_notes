#-*- coding:utf8 -*-
"""
用户:
https://www.jisilu.cn/people/list/page-[1-5707]

帖子:
https://www.jisilu.cn/home/explore/sort_type-new__day-0__page-[1-2006]
"""

import requests
import re

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

class jiSiLu(object):
    def __init__(self):
        print "正在爬取集思录帖子。。。"

    def getSource(self,url):
        html =  requests.get(url,headers=headers).content
        return html

    def getPosts(self,source):
        posts = re.findall('<div class="aw-item">(.*?)</div>',source,re.S)
        return posts

    def changePage(self,url,total_page):
        now_page = int(re.search('page-(\d+)',url,re.S).group(1))
        page_list = []
        for pageNum in range(now_page,total_page+1):
            link = re.sub('page-(\d+)','page-%s' % pageNum,url,re.S)
            page_list.append(link)
        return page_list

    def getInfo(self,post):
        info = {}
        info['title'] = re.search('<a target="_blank" href="(.*?)">(.*?)</a>',post,re.S).group(2)
        info['url']  = re.search('<a target="_blank" href="(.*?)">(.*?)</a>',post,re.S).group(1)
        print info['title'] + ': ' + info['url']
        return info



if (__name__ == '__main__'):

    jisilu = jiSiLu()

    url = "https://www.jisilu.cn/home/explore/sort_type-new__day-0__page-1"
    html = jisilu.getSource(url)
    posts = jisilu.getPosts(html)
    for post in posts:
        jisilu.getInfo(post)



