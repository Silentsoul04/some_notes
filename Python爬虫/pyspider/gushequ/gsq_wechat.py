#-*- coding:utf-8 -*-

import requests
import time
import json
import re
import time
import random
import datetime
import MySQLdb


"""
爬取微信公众号文章信息
"""

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

def save_img(url,cover_name):
    img = requests.get(url)
    print "正在保存: " + cover_name
    with open("img//" + cover_name, 'wb') as f:
        f.write(img.content)
        f.close()

def get_cover_name(datetime,cover):
    img_name = re.sub(r"-| |:","",datetime)
    try:
        img_format = re.search("wx_fmt=(.*?)$",cover,re.S).group(1)
    except AttributeError as e:
        img_format = 'png'
    return img_name + "." + img_format


def save_archive(id, datetime ,title, digest, content_url, cover, content,source_url):
    try:
        conn = MySQLdb.connect(host='139.199.197.243', user='gushequ', passwd='gushequ123', charset='utf8', port=3306)
        cur = conn.cursor()
        # cur.select_db('mysql')
        conn.select_db('gushequ')
        value = [id, datetime,title,digest,content_url,cover,content,source_url]
        print "正在将id为%s的文章插入数据库" % id
        cur.execute("insert into gushequ(id,datetime,title,digest,content_url,cover,content,source_url) values(%s,%s,%s,%s,%s,%s,%s,%s);", value)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print 'Mysql Error Msg:', e

def get_content(url,headers,cookies,params):
    rep_row = requests.get(url,headers=headers,params=params,cookies=cookies).content
    rep = eval(rep_row)
    return rep_row


random.seed(datetime.datetime.now())
count_page = 0
frommsgid = 1000000180

while frommsgid>0:
    headers =  {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I8160 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/6.3.30.920 NetType/WIFI Language/zh_CN",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN, en-US",
        "Accept-Charset": "utf-8, iso-8859-1, utf-16, *;q=0.7"}

    cookies = {
    "malluin":"MTUyNTY1MDYxMA==",
    "mallkey":"d3feb59da89e7994c18261a4996437aee5613a1a987ac1409aa4957ec4b90259f1ae39f0bb4879d8eb19857a373aac94e8856ba85be4d1275473051495a1ddc7b6b556d0cc74726cef43df7c5b6992a0",
    "wxtokenkey":"11b8fb1e8219bfab107a220d4b92e76f308f7536124294fc88389f1c282c55a0",
    "wxticket":"2503598184",
    "wxticketkey":"0e09803bdda6a4382be8767f34436bef308f7536124294fc88389f1c282c55a0",
    "wap_sid":"CLKpvtcFEkBaUU5BV25jMHRaU25wa09CVWNoOVdvbjRjWHp5YjJmWWZMbXBGUjhSelY5ck5hMy0yT002aUlDQ01JNkJZVktJGAQg/BEozILN9AgwpbrJwgU=",
    "wap_sid2":"CLKpvtcFElxQUlBtaUl5NlM1U1l0TG40UWZfRGNrTGRxaHoxX2NMWUJBR1g2RmN0Ry1ZcGZNck8zSmtjdzQwT3QzM2RtbHdRZXJKbWh2M01SWncxZTQ4b2lTanAybk1EQUFBfg=="
    }



    params = {
        "__biz":"MjM5MjAxNTE4MA==",
        "uin":"MTUyNTY1MDYxMA==",
        "key":"d3feb59da89e79949ae5fc44a6ee7f970c55cdb3b0406ab6ed87eede889da19b2fca19c2cac50225a5999d1f106a32aefccd5f286bad8f47330ffbc872c15a17ff06c550ec907c1f6bb6e5e4d74cb965",
        "f":"json",
        "frommsgid":str(frommsgid),
        "count":"10",
        "pass_ticket":"76kvCSCmPrX5NotYXLv12hizlZxH8Yq9pcfoAeRNxGKC+RrudcWjfwJpaZKvsg9W",
        "wxtoken":"",
        "x5":"0"}

    session = requests.session()
    html = session.get("https://mp.weixin.qq.com/mp/getmasssendmsg",headers=headers,params=params,cookies=cookies).content


    archives = eval(html)
    archive_list = eval(archives["general_msg_list"])["list"]


    for archive_info in archive_list:
        try:
            url_row = archive_info["app_msg_ext_info"]["content_url"]
            url = re.sub(r"\\|amp;","",url_row)
            title = archive_info["app_msg_ext_info"]["title"]
            digest = archive_info["app_msg_ext_info"]["digest"]
            cover_row = archive_info["app_msg_ext_info"]["cover"]
            cover = re.sub(r"\\","",cover_row)
            datetime = timestamp_datetime(archive_info["comm_msg_info"]["datetime"])
            id = archive_info["comm_msg_info"]["id"]
            content = get_content(url,headers,cookies,params)
            source_url = re.sub(r"\\","",archive_info["app_msg_ext_info"]["source_url"])
            # save_archive(id, datetime ,title, digest, url, cover, content,source_url)
            # cover_name = get_cover_name(datetime,cover)
            # save_img(cover,cover_name)
            # print "标题: " + title
            # print "链接: " + url
            # print "封面: " + cover
            # print "发布时间: " + datetime
            # print "文章id：" + str(id)
            # print "#########################"
            # print source_url
            # time.sleep(random.random() * 5)
            print content
        except KeyError as e:
            title = "这是糙版"
            digest = None
            url = None
            cover = None
            source_url = None
            datetime = timestamp_datetime(archive_info["comm_msg_info"]["datetime"])
            id = archive_info["comm_msg_info"]["id"]
            content = archive_info["comm_msg_info"]["content"]
            # save_archive(id, datetime, title, digest, url, cover, content,source_url)
            # print title
            # print "发布时间: " + datetime
            # print "文章id：" + str(id)
            # print "#########################"
            print content
    frommsgid = id
    count_page += 1
    time.sleep(random.random()*10)
    print "******************************************************************"
    break