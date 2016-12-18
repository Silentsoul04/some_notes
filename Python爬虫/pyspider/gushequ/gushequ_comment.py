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
    return rep

def get_comments(appmsgid,comment_id,cookies,headers):
    api = "https://mp.weixin.qq.com/mp/appmsg_comment"
    params = {"action": "getcomment",
              "__biz": "MjM5MjAxNTE4MA==",
              "appmsgid": str(appmsgid),
              "idx": "1",
              "comment_id": str(comment_id),
              "offset": "0",
              "limit": "100",
              "uin": "MTUyNTY1MDYxMA%3D%3D",
              "key": "d3feb59da89e79943305bb1b14d5d6fc36d0dd94002daa87b3651263a560cda0bd03d45569b0e659d443d6bbd3f03abd8f00d39d985812271d06199ecef61eedd1ba737e5e6822cfe118052ec3a16fd4",
              "pass_ticket": "LV10oE60VNJ5r8RXAnGlV43MWSfzlCL136Ei%252Bhm4cov8KWBsWFE0B1WE8KL5ZH7C",
              "wxtoken": "298440671",
              "devicetype": "android-17",
              "clientversion": "26031e30",
              "x5": "0"}
    response = requests.get(api,headers=headers,cookies=cookies,params=params)
    return response.content

def formart_comment(response,title,datetime):
    rep = eval(response)
    comments = rep["elected_comment"]
    count = 1
    print title + ":(" + datetime+ ")"
    print "============================================="
    for comment in comments:
        try:
            reply_content = re.sub(r"\\", "", comment["reply"]["reply_list"][0]["content"])
        except IndexError as e:
            reply_content = "000000"
        comment_content = re.sub(r"\\", "", comment["content"])
        print "评论%s: " % (count) + comment_content
        print "答复：" + reply_content + "\n"
        count += 1

def save_comment(response,title,archive_datetime):
    rep = eval(response)
    comments = rep["elected_comment"]
    print "正在存储%s的评论..." % (title)
    for comment in comments:
        nick_name = comment["nick_name"]
        logo_url = re.sub(r"\\|132", "",comment["logo_url"])
        comment_content = re.sub(r"\\", "", comment["content"])
        try:
            reply_content = re.sub(r"\\", "", comment["reply"]["reply_list"][0]["content"])
        except IndexError as e:
            reply_content = "000000"
        # print title + " " + archive_datetime
        # print nick_name
        # print logo_url
        # print comment_content
        # print reply_content
        try:

            conn = MySQLdb.connect(host='139.199.197.243', user='gushequ', passwd='gushequ123', charset='utf8', port=3306)
            cur = conn.cursor()
            # cur.select_db('mysql')
            conn.select_db('gushequ')
            value = [title, archive_datetime, nick_name, logo_url, comment_content, reply_content]
            cur.execute("insert into gushequ_comments(title, archive_datetime,nick_name,logo_url,comment_content,reply_content) values(%s,%s,%s,%s,%s,%s);", value)
            conn.commit()
            cur.close()
            conn.close()
        except MySQLdb.Error, e:
            print 'Mysql Error Msg:', e

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
    "mallkey":"c81d77271180a0e691a8a1e6515ccfc0cf5b00303880d4d2e26ec812997f9d3613adc13e5892d3627edd1552212759682e019a59e9c7750b96a6e44a3202f7ab3058046b71bb23447f996b6aabe4d46d",
    "wxtokenkey":"57b6095a31654a98884e5e91598febd3976fffa3e5462177cfe6e34b146223fb",
    "wxticket":"1013746203",
    "wxticketkey":"9081edbd72bda4426db1546d0d03bc65976fffa3e5462177cfe6e34b146223fb",
    "wap_sid":"CLKpvtcFEkAyNlFBTXc4WEdoTHhRZllZS1p3bGh5VV9vbzZ5N01iQjJlN0w3LXJfN09zWE9Fd1preTdKZmpMb2NWMWtBOHlIGAQg/BEozILN9AgwxuLKwgU=",
    "wap_sid2":"CLKpvtcFElw0bHFlR285amVJTWRwY1VkTU9BRXNvS213MVB1TVE1bnFOWWFGSnhFZ2loaFhvcDliQWJ6NUN0WGhTMjhIcDc3aVlZSGJlVUJrdER2X1BlWENpQ0tSWE1EQUFBfg=="
    }

    params = {
        "__biz":"MjM5MjAxNTE4MA==",
        "uin":"MTUyNTY1MDYxMA==",
        "key":"c81d77271180a0e691a8a1e6515ccfc0cf5b00303880d4d2e26ec812997f9d3613adc13e5892d3627edd1552212759682e019a59e9c7750b96a6e44a3202f7ab3058046b71bb23447f996b6aabe4d46d",
        "f":"json",
        "frommsgid":str(frommsgid),
        "count":"10",
        "pass_ticket":"LV10oE60VNJ5r8RXAnGlV43MWSfzlCL136Ei%252Bhm4cov8KWBsWFE0B1WE8KL5ZH7C",
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
            link = content["link"]
            mid = re.search('mid=(\d+).*',link).group(1)
            comment_id = content["comment_id"]
            comments_response = get_comments(mid,comment_id,cookies,headers)
            save_comment(comments_response,title,datetime)
        except KeyError as e:
            pass
    frommsgid = id
    count_page += 1
    time.sleep(random.random()*10)