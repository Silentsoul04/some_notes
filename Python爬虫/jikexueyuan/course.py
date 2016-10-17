#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

req = requests.get("http://www.jikexueyuan.com/course/?pageNum=1")

bsObj = BeautifulSoup(req.text, "html.parser")
print bsObj.find("div",{"class":"lesson-list"})