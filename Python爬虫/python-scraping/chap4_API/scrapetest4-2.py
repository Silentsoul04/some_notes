from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html.read(),"html.parser")
    links = bsObj.find("div",id="bodyContent").find_all("a",{"href":re.compile("^(/wiki)((?!:).)*$")})
    return links

def getHistoryIPs(pageUrl):
    # 编辑历史页面的url是
    # https://en.wikipediaorg./w/index.php?title=Python&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    #　找出class属性是 "mw-userlink mw-anonuserlink"的链接
    # 它们用IP地址代替用户名
    ipAddresses = bsObj.find_all("a",{"class":"mw-userlink mw-anonuserlink"})

    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python")

while len(links) > 0:
    for link in links:
        print("--------------------------------------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            # pattern = re.compile("[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}")
            # historyIP = pattern.findall(historyIP)
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)
    newLink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newLink)