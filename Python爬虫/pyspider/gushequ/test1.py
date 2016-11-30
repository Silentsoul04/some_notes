#-*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

url = "http://www.gushequ.cc/archives/"

html = requests.get(url).content

def getImgUrl(html):
    imgUrl = re.findall('src="http://www.zixinke.cn/wp-content/uploads/2016/11/(.*?)" ',html,re.S)
    return imgUrl

bsObj = BeautifulSoup(html, "html.parser")
archives = bsObj.find("article").findAll("a")

articleUrls = []

for archive in archives:
    articleUrl = archive.attrs["href"]
    articleUrls.append(articleUrl)

for articleUrl in articleUrls:
    html = requests.get(articleUrl).content
    imgUrls = getImgUrl(html)
    print articleUrl
    for image in imgUrls:
        imgUrl = "http://www.zixinke.cn/wp-content/uploads/2016/11/" + image
        img = requests.get(imgUrl)
        print "正在保存: " + image
        with open("img\\" + image, 'wb') as f:
            f.write(img.content)
            f.close()