# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import MySQLdb

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

def getStockList(url):
    response = requests.get(url,headers=headers)
    response.encoding = "gbk"
    bsObj = BeautifulSoup(response.text, "html.parser")
    stock_list = bsObj.find("div",{"class":"quotebody"}).find_all("li")
    return stock_list

def getStockCode(stock):
    stock_code = re.search('\((\d+)\)',stock).group(1)
    return stock_code

def getStockName(stock):
    stock_name = re.search(r'^(.*?)\(',stock).group(1)
    return stock_name

def checkIsStock(stock_code):   ##判断是否是股票代码
    """
    上交所: 600,601,603 开头
    深交所: 000,002,300 开头
    """
    if stock_code.startswith(('600','601','603','000','002','300')):
        return True
    else:
        return False
def getStockMarket(stock_code):
    if stock_code.startswith(('600','601','603')):
        return 'sh'
    elif stock_code.startswith(('000','002','300')):
        return 'sz'
def saveData(code,name,market):
    try:
        conn = MySQLdb.connect(host='139.199.197.243', user='gushequ', passwd='gushequ123', charset='utf8', port=3306)
        cur = conn.cursor()
        # cur.select_db('mysql')
        conn.select_db('gushequ')
        value = [code,name,market]
        cur.execute("insert into stock_list(code,name,market) values(%s,%s,%s);",value)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print 'Mysql Error Msg:', e

sz_stock_url = "http://quote.eastmoney.com/stock_list.html"
sz_stock = getStockList(sz_stock_url)
for each_stock in sz_stock:
    stock = each_stock.get_text()
    stock_code = getStockCode(stock)
    stock_name = getStockName(stock)
    stock_market = getStockMarket(stock_code)
    if checkIsStock(stock_code):
        saveData(stock_code,stock_name,stock_market)
        print stock_market + stock_code + " : " + stock_name


