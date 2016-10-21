#-* coding:utf-8 -*-

import requests
import json
import time


def formatjson(fundajson):
    # 格式化集思录返回的json数据,以字典形式保存
    d = {}
    for row in fundajson['rows']:
        id = row['id']
        cell = row['cell']
        d[id] = cell
    return d

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6"}

# 获取unix时间戳
unixTime = int(time.time()*1000)

# 分级A数据
# 返回的字典格式
# { 150020:
# {'abrate': '5:5',
#  'calc_info': None,
#  'coupon_descr': '+3.0%',
#  'coupon_descr_s': '+3.0%',
#  'fund_descr': '每年第一个工作日定折，无下折，A不参与上折，净值<1元无定折',
#  'funda_amount': 178823,
#  'funda_amount_increase': '0',
#  'funda_amount_increase_rt': '0.00%',
#  'funda_base_est_dis_rt': '2.27%',
#  'funda_base_est_dis_rt_t1': '2.27%',
#  'funda_base_est_dis_rt_t2': '-0.34%',
#  'funda_base_est_dis_rt_tip': '',
#  'funda_base_fund_id': '163109',
#  'funda_coupon': '5.75',
#  'funda_coupon_next': '4.75',
#  'funda_current_price': '0.783',
#  'funda_discount_rt': '24.75%',
#  'funda_id': '150022',
#  'funda_increase_rt': '0.00%',
#  'funda_index_id': '399001',
#  'funda_index_increase_rt': '0.00%',
#  'funda_index_name': '深证成指',
#  'funda_left_year': '永续',
#  'funda_lower_recalc_rt': '1.82%',
#  'funda_name': '深成指A',
#  'funda_nav_dt': '2015-09-14',
#  'funda_profit_rt': '7.74%',
#  'funda_profit_rt_next': '6.424%',
#  'funda_value': '1.0405',
#  'funda_volume': '0.00',
#  'fundb_upper_recalc_rt': '244.35%',
#  'fundb_upper_recalc_rt_info': '深成指A不参与上折',
#  'last_time': '09:18:22',
#  'left_recalc_year': '0.30411',
#  'lower_recalc_profit_rt': '-',
#  'next_recalc_dt': '<span style="font-style:italic">2016-01-04</span>',
#  'owned': 0,
#  'status_cd': 'N'}
# }

# 请求
url = "https://www.jisilu.cn/data/sfnew/funda_list/%s" % str(unixTime)
rep = requests.get(url,headers=headers)

# 获取返回的json字符串
fundajson = json.loads(rep.text)

fundadata = formatjson(fundajson)

for id,data in fundadata.items():
    print("-------------------------------------")
    print(id)
    print("#######")
    for key,value in data.items():
        print(key + " : " +str(value))