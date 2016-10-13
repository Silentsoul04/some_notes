from urllib.request import urlopen
from urllib.error import URLError,HTTPError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import datetime

"""
urlparse(urlstring[, scheme[, allow_fragments]])
urlparse将urlstring解析成6个部分
它从urlstring中取得URL，并返回元组 (scheme, netloc, path, parameters, query, fragment)

>>> url = urlparse("http://www.ichenfei.com/")
>>> print (url)
ParseResult(scheme='http', netloc='www.ichenfei.com', path='/', params='', query='', fragment='')

scheme:协议
netloc：域名or ip地址
path：网站目录

"""

pages = set()
random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()

def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # 找到所有 / 开头的链接
    links = bsObj.find_all("a",{"href":re.compile("^(/|.*"+includeUrl+")")})
    for link in links:
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if(link.attrs["href"].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks

#获取页面所有外链列表:
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    links = bsObj.find_all("a",{"href":re.compile("^(http|www)((?!"+excludeUrl+").)*$")})
    for link in links:
        if(link.attrs["href"] is not None):
            if(link.attrs["href"] not in externalLinks):
                externalLinks.append(link.attrs["href"])

    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("此页面没有外链,正在随机查找一个内链...")
        domain = urlparse(startingPage).scheme + "//" + urlparse(startingPage).netloc
        internalLinks = getExternalLinks(bsObj, domain)
        if len(internalLinks) == 0:
            print("此页面也没有内链，正在前往此网站官网寻找外链...")
            getRandomExternalLink(domain)
        else:
            return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj,siteUrl)
    externalLinks = getExternalLinks(bsObj,siteUrl)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
        print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的URL是："+link)
        allIntLinks.add(link)
        getAllExternalLinks(link)


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("随机得到的外链是: " + externalLink)
    followExternalOnly(externalLink)


getAllExternalLinks("http://oreilly.com")