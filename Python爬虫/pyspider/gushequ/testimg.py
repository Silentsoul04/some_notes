#-*- coding:utf-8 -*-

import requests
import re

url = "http://www.zixinke.cn/2016/11/%E4%BB%8A%E6%99%9A%E6%8E%A8%E8%8D%90%E4%B8%80%E7%B1%BB%E8%82%A1%E7%A5%A8%EF%BC%8820161122%EF%BC%89/"
html = requests.get(url).content

def getImgUrl(html):
    imgUrl = re.findall('src="http://www.zixinke.cn/wp-content/uploads/2016/11/(.*?)" alt="',html,re.S)
    return imgUrl

img = requests.get(imgUrl)

local_filename = '22-8.png'

with open("img\\" + local_filename, 'wb') as f:
    f.write(img.content)
    f.close()