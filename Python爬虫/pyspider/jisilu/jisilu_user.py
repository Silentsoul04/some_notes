#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
用户:
https://www.jisilu.cn/people/list/page-[1-5707]
"""

import requests
import re
import MySQLdb



class Jisilu_User():
    def __init__(self,url):
        print "正在爬取: %s" %(url)
    def getUserInfo(self,rep):
        user_infos = re.findall('<div class="aw-item">.*?</div>',rep,re.S)
        return user_infos
    def getUserName(self,user_info):
        user_name = re.search(' class="aw-user-name">(.*?)</a>',user_info).group(1)
        return user_name
    def getUserPrestige(self,user_info):
        user_prestige = re.search('威望: <em class="aw-text-color-green">(.*?)</em></span>',user_info).group(1)
        return user_prestige
    def getUserApprove(self,user_info):
        user_approve = re.search('赞同: <em>(.*?)</em></span>',user_info).group(1)
        return user_approve
    def getUserThank(self,user_info):
        user_thank = re.search('感谢: <em>(.*?)</em></span>',user_info).group(1)
        return user_thank
    def getUserIntro(self,user_info):
        user_intro = re.search('class="aw-user-name">(.*?)</a>(.*?)</p>',user_info,re.S).group(2)
        user_introduction = re.sub(r'\t|\n|','',user_intro)
        return user_introduction
    def saveData(self,user_name,user_prestige,user_approve,user_thank,introduction):
        try:
            conn = MySQLdb.connect(host='t.ichenfei.com', user='jisilu', passwd='jisilu123', charset='utf8', port=3306)
            cur = conn.cursor()
            # cur.select_db('mysql')
            conn.select_db('jisilu')
            # id,post_author,post_date,post_date_gmt,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,post_password
            # post_name,to_ping,pinged,post_modified,post_modified_gmtpost_content_filtered,post_parent,guid,menu_order
            # post_type,post_mime_type,comment_count
            value = [user_name, user_prestige, user_approve, user_thank,introduction]
            cur.execute("insert into jisilu_user(user_name,prestige,approve,thank,introduction) values(%s,%s,%s,%s,%s);",value)
            conn.commit()
            cur.close()
            conn.close()

        except MySQLdb.Error, e:
            print 'Mysql Error Msg:', e


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
}

for page in range(2,5929):
    url = "https://www.jisilu.cn/people/list/page-%s" % (page)
    user = Jisilu_User(url)
    session = requests.session()
    rep = session.get(url,headers=headers).content
    user_infos = user.getUserInfo(rep)

    for user_info in user_infos:
        # print "用户名: " + user.getUserName(user_info)
        # print "威望: " + user.getUserPrestige(user_info)
        # print "赞同: " + user.getUserApprove(user_info)
        # print "感谢: " + user.getUserThank(user_info)
        # print "介绍: " + user.getUserIntro(user_info)
        # print "#######################"
        user_name = user.getUserName(user_info)
        user_prestige = user.getUserPrestige(user_info)
        user_approve = user.getUserApprove(user_info)
        user_thank = user.getUserThank(user_info)
        introduction = user.getUserIntro(user_info)
        print "正在将 %s 插入数据库..." % (user_name)
        user.saveData(user_name,user_prestige,user_approve,user_thank,introduction)


