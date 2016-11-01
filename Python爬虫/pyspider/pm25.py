#-*- coding:utf-8 -*-
import urllib2
from time import ctime
from bs4 import BeautifulSoup


def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    html = urllib2.urlopen(site)
    soup = BeautifulSoup(html, "html.parser")

    city = soup.find(class_ = 'bi_loaction_city')
    aqi = soup.find("a",{"class","bi_aqiarea_num"})
    quality = soup.select(".bi_aqiarea_right span")
    result = soup.find("div",class_ = "bi_aqiarea_bottom")

    print city.text + u"\nAQI指数： " + aqi.text + u"\n空气质量: " + quality[0].text + result.text
    print '*'*20 +ctime()+'*'*20

if __name__ == "__main__":
    getPM25('beijing')