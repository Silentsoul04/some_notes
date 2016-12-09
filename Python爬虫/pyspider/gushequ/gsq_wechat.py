#-*- coding:utf-8 -*-

import requests
import time
import json
import re
import time
import random
import datetime

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
    img_format = re.search("wx_fmt=(.*?)$",cover,re.S).group(1)
    return img_name + "." + img_format

random.seed(datetime.datetime.now())
count_page = 0
frommsgid = 206633550
while frommsgid>0:
    headers =  {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I8160 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/6.3.30.920 NetType/WIFI Language/zh_CN",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN, en-US",
        "Accept-Charset": "utf-8, iso-8859-1, utf-16, *;q=0.7"}

    cookies = {
    "malluin":"MTUyNTY1MDYxMA==",
    "mallkey":"9ed31d4918c154c84b64e3e51f32628117a78eeda6217538cd3dc98e5e29c0a44ebf252300492e849ba4f3c76a2a32154215407adb26c6db2a0cf85781c6e5f2446dfb698b477f50fca3a788bcbb3f8d",
    "wxtokenkey":"48edd5958dc55a71afa3d4dd786db11cead27fccb4fbe6ffcfc34a1884aeab87",
    "wxticket":"1826103214",
    "wxticketkey":"21b7ee26f5d8a7dd9fa200bf41a210c6ead27fccb4fbe6ffcfc34a1884aeab87",
    "wap_sid":"CLKpvtcFEkBHaDE5d2pZeVFMSnhrU2RfYUtVQVpMcUo1VmpqbzRZR0lKcFhKZXZPTlhCbUJrVHlnWXpva3NRR3ZVRy1VT2E1GAQg/REozILN9AgwrPKjwgU=",
    "wap_sid2":"CLKpvtcFElxSOHllZ19TMU92RUJudVlmc0pZbUNXY0d0LUh4SGY5V01ZQ1FWMmRMZ01nNV9PX3piOXFLQ2VJcjBtYlZTY2ZOVWQ0V1poTTB3a1J1LVlhSFZZYUNLSElEQUFBfg=="
    }


    params = {
        "__biz":"MjM5MjAxNTE4MA==",
        "uin":"MTUyNTY1MDYxMA==",
        "key":"9ed31d4918c154c81c1e47402cf4b886216491e2b7595ab1a147c8e086453998191c7ddaa2fe3c356587ceadbab16332b2b62efc3d8018048893f0d90336be98ff78f3cd6781346e1c0e2a5590b4c848",
        "f":"json",
        "frommsgid":str(frommsgid),
        "count":"10",
        "pass_ticket":"i%252Bw8A%252B49swaRAgzn7XmBucHYj%252F64YTYyQqwTihGjFKX21uLdN8cVKgPjgFu%252FxxKM",
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
            cover_row = archive_info["app_msg_ext_info"]["cover"]
            cover = re.sub(r"\\","",cover_row)
            datetime = timestamp_datetime(archive_info["comm_msg_info"]["datetime"])
            id = archive_info["comm_msg_info"]["id"]

            # cover_name = get_cover_name(datetime,cover)
           # save_img(cover,cover_name)
            print "标题: " + title
            print "链接: " + url
            print "封面: " + cover
            print "发布时间: " + datetime
            print "文章id：" + str(id)
            print "#########################"
        except KeyError as e:
            title = "这是简版。"
            datetime = timestamp_datetime(archive_info["comm_msg_info"]["datetime"])
            id = archive_info["comm_msg_info"]["id"]
            print title
            print "发布时间: " + datetime
            print "文章id：" + str(id)
            print "#########################"
    frommsgid = id
    count_page += 1
    time.sleep(random.random()*10)
    print "******************************************************************"