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
def save_comment(command_content,):
    pass

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
    "mallkey":"d3feb59da89e799405044e6e732ef414a32e02d4e20f40f3afb0af73ae25a137f267211766b3587cb368ee79d0a87573b8399d49540175ab81a4027d3a09bcd5c8e1590aad99133075e6c62a01830c63",
    "wxtokenkey":"c1c290a16782a1baa6de7c034a64aa653d31375366aa41b64051ef0f32382aa4",
    "wxticket":"1027865461",
    "wxticketkey":"362437c15450edfaef7be7b802937c2b3d31375366aa41b64051ef0f32382aa4",
    "wap_sid":"CLKpvtcFEkA3THVnN3YtZUhNOWV0cEVEQnBBMkw0RFhoMFAxT1hCYnMwM3JlUFkzN05DamRvX0lkSE5EaFdRS19yX2hjeFJsGAQg/BEozILN9Agw8PbJwgU=",
    "wap_sid2":"wap_sid2=CLKpvtcFElxRVGtZOXBoaUtsZUZzbkZSYzJNZ2N3SnpzcDFXNEl2RnpJYWlhcWFaZmxzV0F0b3c3OHJjN3hFcTJrSEh0RDY3Q0g5ZzFGeEFhLUFmRDdUZnVER0JQbk1EQUFBfg=="
    }

    params = {
        "__biz":"MjM5MjAxNTE4MA==",
        "uin":"MTUyNTY1MDYxMA==",
        "key":"d3feb59da89e799405044e6e732ef414a32e02d4e20f40f3afb0af73ae25a137f267211766b3587cb368ee79d0a87573b8399d49540175ab81a4027d3a09bcd5c8e1590aad99133075e6c62a01830c63",
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
            comments = get_comments(mid,comment_id,cookies,headers)
            formart_comment(comments,title,datetime)
        except KeyError as e:
            pass
    frommsgid = id
    count_page += 1
    time.sleep(random.random()*10)