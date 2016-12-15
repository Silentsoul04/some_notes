#-*- coding:utf-8 -*-

import requests
import MySQLdb
#获取东方财富网的定增数据

api = "http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx"

page = 1
def save_data(code,name,type,volume,issue_price,new_price,issue_date,listing_date,period):
    try:
        conn = MySQLdb.connect(host='139.199.197.243', user='gushequ', passwd='gushequ123', charset='utf8', port=3306)
        cur = conn.cursor()
        # cur.select_db('mysql')
        conn.select_db('gushequ')
        value = [code,name,type,volume,issue_price,new_price,issue_date,listing_date,period]
        cur.execute("insert into dingzeng(code,name,type,volume,issue_price,new_price,issue_date,listing_date,period) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);", value)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print 'Mysql Error Msg:', e

for page in range(1,55):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Accept": "*/*",
        "Referer": "http://data.eastmoney.com/other/qbzf.html",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
    }
    params = {
        "type":"SR",
        "sty":"ZF",
        "st":"1",
        "sr":"1",
        "p":str(page),
        "ps":"50",
        "stat":"1",
        "js":'{"pages":(pc),"data":[(x)]}'
    }

    session = requests.Session()

    response = session.get(api,headers=headers,params=params).content
    response = eval(response)
    # for dingzeng_stock in dingzeng_list:
    #     print dingzeng_stock
    print "第%s页: " % page
    for dingzeng_stock in response["data"]:
        code =  dingzeng_stock.split(',')[0]
        name = dingzeng_stock.split(',')[1]
        type = dingzeng_stock.split(',')[2]
        volume = dingzeng_stock.split(',')[3]
        issue_price = dingzeng_stock.split(',')[4]
        new_price = dingzeng_stock.split(',')[5]
        issue_date = dingzeng_stock.split(',')[6]
        listing_date = dingzeng_stock.split(',')[7]
        period = dingzeng_stock.split(',')[16]
        print str(code) + " " + str(name)  + " " + str(type) + " " + str(volume)  + " " + str(issue_price)  + " " + str(new_price)  + " " + str(issue_date)  + " " + str(listing_date)  + " " + str(period)
        save_data(code,name,type,volume,issue_price,new_price,issue_date,listing_date,period)