# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup


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
    return stock_code

def checkIsStock(stock_code):
    pass



sz_stock_url = "http://quote.eastmoney.com/stock_list.html#sz"
sz_stock = getStockList(sz_stock_url)
for each_stock in sz_stock:
    stock = each_stock.get_text()
    stock_code = getStockCode(stock)
    stock_name = getStockName(stock)
    print stock_code + " : " + stock_name

