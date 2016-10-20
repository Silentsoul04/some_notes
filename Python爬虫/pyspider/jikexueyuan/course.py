#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

class JikeSpider(object):
    def __init__(self):
        print u"开始爬取内容......"

    def getSource(self,url):
        html = requests.get(url,headers = headers)
        return html.content

    def changePage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for pageNum in range(now_page,total_page+1):
            link = re.sub('pageNum=(\d+)','pageNum=%s' % pageNum,url,re.S)
            page_group.append(link)
        return page_group

    def getEveryClass(self,source):
        every_class = re.findall('<li id=(.*?)</li>',source,re.S)
        return every_class

    def getInfo(self,eachClass):
        info = {}
        info['title'] = re.search('title="(.*?)" alt',eachClass,re.S).group(1)
        content = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachClass,re.S).group(1)
        info['content'] = re.sub(r'\t|\n','',content)
        timeandlevel = re.findall('<em>(.*?)</em>',eachClass,re.S)
        info['time'] = re.sub(r'\t|\n','',timeandlevel[0])
        info['classlevel'] = timeandlevel[1]
        info['classnum'] = re.search('<em class="learn-number">(.*?)</em>',eachClass,re.S).group(1)
        info['classurl'] = re.search('<a href="(.*?)" target="_blank"',eachClass,re.S).group(1)
        return info

    def saveInfo(self,classinfo):
        f = open('jikeCourseInfo.txt','a')
        for each in classinfo:
            f.writelines('标题: ' + each['title'] + '\n')
            f.writelines('简介: ' + each['content'] + '\n')
            f.writelines('课时： ' + each['time'] + '\n')
            f.writelines('课程链接: ' + each['classurl'] + '\n')
            f.writelines('课程等级：' + each['classlevel'] + '\n')
            f.writelines('课程选修人数: ' + each['classnum'] + '\n\n')
        f.close()



if __name__ == '__main__':

    classinfo = []
    url = "http://www.jikexueyuan.com/course/?pageNum=1"
    jikespider = JikeSpider()
    all_links = jikespider.changePage(url,94)

    for link in all_links:

        print '正在处理页面:' + link
        html = jikespider.getSource(link)
        everyclass = jikespider.getEveryClass(html)
        for each in everyclass:
            info = jikespider.getInfo(each)
            classinfo.append(info)

    jikespider.saveInfo(classinfo)

    # url = "http://www.jikexueyuan.com/course/?pageNum=1"
    # jikespider = JikeSpider()
    # html = jikespider.getSource(url)
    # everyclass = jikespider.getEveryClass(html)
    # #print everyclass
    # for each in everyclass:
    #     print "==============================================================="
    #     print jikespider.getInfo(each)['title']
    #     print jikespider.getInfo(each)['classurl']
    #     print jikespider.getInfo(each)['content']
    #     print jikespider.getInfo(each)['time']
    #     print jikespider.getInfo(each)['classlevel']
    #     print jikespider.getInfo(each)['classnum']
