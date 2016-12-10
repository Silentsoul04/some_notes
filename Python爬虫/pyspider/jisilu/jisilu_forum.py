#-*- coding:utf8 -*-
"""
用户:
https://www.jisilu.cn/people/list/page-[1-5707]

帖子:
https://www.jisilu.cn/home/explore/sort_type-new__day-0__page-[1-2006]
"""

import requests
import re
import MySQLdb

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

class jiSiLu(object):
    def __init__(self):
        pass
    def getSource(self,url):
        session = requests.session()
        response =  session.get(url,headers=headers).content
        return response

    def getTitle(self,html):
        title = re.search('<h1>(.*?)</h1>',html,re.S).group(1)
        return title

    # def getContent(self,html):
    #     content = re.search('<div class="aw-mod-body">(.*?)<div class="aw-question-detail-meta">',html,re.S).group(1)
    #     return content

    def getPostUser(self,html):
        user_name = re.search('<dd class="pull-left">(.*?)data-id="(\d)+">(.*?)</a>',html,re.S).group(3)
        return user_name

    def getPostDate(self,html):
        post_date = re.search('<div class="aw-question-detail-meta">(.*?)<span class="pull-left aw-text-color-999">(.*?)</span>',html,re.S).group(2)
        return  post_date

    def getPostStatus(self,html): #最新回复时间，浏览数,关注数
        stauts = {}
        new_reply_date = re.search('最新活动: <span class="aw-text-color-blue">(.*?)</span>',html,re.S).group(1)
        views = re.search('浏览: <span class="aw-text-color-blue">(.*?)</span>',html,re.S).group(1)
        attention = re.search('关注: <span class="aw-text-color-blue">(.*?)</span>',html,re.S).group(1)
        stauts['new_reply_date'] = new_reply_date
        stauts['views'] = views
        stauts['attentions'] = attention
        return stauts

    def getReplys(self,html):
        replys = re.search('<h2>(\d+) 个回复</h2>',html,re.S).group(1)
        return replys

    def saveData(self,id,title,post_user,post_date,new_reply_date,replys,views,attentions,url):
        try:
            conn = MySQLdb.connect(host='139.199.197.243', user='jisilu', passwd='jisilu123', charset='utf8',port=3306)
            cur = conn.cursor()
            # cur.select_db('mysql')
            conn.select_db('jisilu')
            value = [id,title,post_user,post_date,new_reply_date,replys,views,attentions,url]
            print "正在将id为%s的帖子插入数据库...." % id
            cur.execute("insert into jisilu_forum(id,title,post_user,post_date,new_reply_date,replys,views,attentions,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);",value)
            conn.commit()
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print 'Mysql Error Msg:', e

if (__name__ == '__main__'):

    jisilu = jiSiLu()
    for id in range(1,81209):
        url = "https://www.jisilu.cn/question/%s" % id
        try:
            html = jisilu.getSource(url)
            title = jisilu.getTitle(html)
            post_user = jisilu.getPostUser(html)
            post_date = jisilu.getPostDate(html)
            replys = jisilu.getReplys(html)
            posts_status = jisilu.getPostStatus(html)
            views = posts_status["views"]
            attentions = posts_status["attentions"]
            new_reply_date = posts_status["new_reply_date"]
            jisilu.saveData(id, title, post_user, post_date, new_reply_date, replys, views, attentions, url)

            print "帖子id：" + str(id)
            print "标题:" + title
            print "发起人: " + post_user
            print "发起时间: " + post_date
            print "最新回复时间: " + new_reply_date
            print "回复数: " + replys
            print "浏览数: " + views
            print "关注数: " + attentions
            print "帖子url: " + url
        except AttributeError as e:
            print "id 为 %s 的帖子不存在。" % id

        print "#######################"
