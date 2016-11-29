#-*- coding:utf-8 -*-

import requests
import json
import re

"""
爬取微信公众号文章
"""

# params = {"__biz":"MjM5MjAxNTE4MA==",
#           "uin":"MTUyNTY1MDYxMA==",
#           "key":"9ed31d4918c154c869301a1b680c247e1cc5574d42a685035c62348e124bbb455d8220989296a6b2bde67e2ec0382f6eaa9d2e461617e46055bcbc2ccba93c4c6c70ede8dee24c428e7782a646e5e6e7",
#           "f":"json",
#           "frommsgid":"1000000150",
#           "count":"10",
#           "pass_ticket":"%25252B2aSSak3jlfrUl2r3M4vcqvdCzzAMtD3%25252FMNh%25252B9wRw%25252FsGvuCsK2Wtwojq9ipMBm2J",
#           "wxtoken":"",
#           "x5":"0"}

headers =  {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I8160 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/6.3.30.920 NetType/WIFI Language/zh_CN",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN, en-US",
    "Accept-Charset": "utf-8, iso-8859-1, utf-16, *;q=0.7"}

session = requests.session()
html = session.get("http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MjAxNTE4MA==&uin=MTUyNTY1MDYxMA==&key=9ed31d4918c154c83059b2dbeedcc3bea214e42ef123d28e5921a193832a774fa145da5883114fa0124e8fc83a4464a2bb60d3ace2370b97c44c2482ff97e2f29733d46f384bbdfbf7668b10905d3744&f=json&frommsgid=1000000140&count=10&uin=MTUyNTY1MDYxMA%3D%3D&key=9ed31d4918c154c83059b2dbeedcc3bea214e42ef123d28e5921a193832a774fa145da5883114fa0124e8fc83a4464a2bb60d3ace2370b97c44c2482ff97e2f29733d46f384bbdfbf7668b10905d3744&pass_ticket=%25252B2aSSak3jlfrUl2r3M4vcqvdCzzAMtD3%25252FMNh%25252B9wRw%25252FsGvuCsK2Wtwojq9ipMBm2J&wxtoken=&x5=0",headers=headers)

print html.content