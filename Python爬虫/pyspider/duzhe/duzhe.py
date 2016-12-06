# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

class DuZhe():
    def __init__(self):
        pass
    def getArticleList(self,url):
        html = requests.get(url, headers=headers)
        html.encoding = "utf-8"
        bsObj = BeautifulSoup(html.text, "html.parser")
        article_urls = bsObj.find("table",{"class":"booklist"}).find_all("a")
        return article_urls
    def getArticleUrlBase(self,url):
        article_url_base = re.sub("index.html","",url)
        return article_url_base


if __name__ == "__main__":
    duzhe = DuZhe()

    base_url = "http://www.52duzhe.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

    html = requests.get(base_url,headers=headers)
    html.encoding = "gb2312"
    bsObj = BeautifulSoup(html.text, "html.parser")
    journals = bsObj.find_all("tr")

    for journal in journals:
        links = journal.find_all("a")

        for link in links:
            print link.get_text()
            bookurl = base_url + link.get("href")
            # print link.get_text() + ": " + bookurl
            for article_url in duzhe.getArticleList(bookurl):
                article_url_base = duzhe.getArticleUrlBase(bookurl)
                print article_url.get_text() + ": " + article_url_base + article_url.get("href")