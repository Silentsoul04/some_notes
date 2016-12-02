#-* coding:utf-8 -*-

import requests
import json
import time

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt

# def datetime_timestamp(dt):
#     #dt为字符串
#     #中间过程，一般都需要将字符串转化为时间数组
#     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
#     ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
#     #将"2012-03-28 06:53:40"转化为时间戳
#     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
#     return int(s)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

jsl_api = "https://www.jisilu.cn/api_v2/fenji/fundm/?ptype=price"
rep = requests.get(jsl_api,headers=headers)

# 获取返回的json字符串
fundjson = json.loads(rep.content)

#
# for id,data in funddata.items():
#     print("-------------------------------------")
#     print(id)
#     print("#######")
#     for key,value in data.items():
#         print(key + " : " +str(value))

now_time = timestamp_datetime(fundjson['timestamp'])

print "当前时间: " + now_time
# for fund_nm,fund_id in funddata.items():
#     print fund_nm + " "+ fund_id

for fund in range(len(fundjson['data'])):
    print "######################################"
    for key,value in  fundjson['data'][fund].items():
        print ("%s : %s" % (key,value))
