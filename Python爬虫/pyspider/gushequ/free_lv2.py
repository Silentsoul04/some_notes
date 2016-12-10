#-*- coding:utf-8 -*-
import requests
import re

def get_all_stock_codes():
    """获取所有股票 ID"""
    all_stock_codes_url = 'http://www.shdjt.com/js/lib/astock.js'
    grep_stock_codes = re.compile('~(\d+)`')
    response = requests.get(all_stock_codes_url)
    stock_codes = grep_stock_codes.findall(response.text)
    return stock_codes

for stock in  get_all_stock_codes():
    print stock