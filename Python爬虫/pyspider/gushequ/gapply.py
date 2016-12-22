#-* coding:utf-8 -*-
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

"""
处理HTTP 接入验证
"""

auth = HTTPBasicAuth('lichuan', 'PasswOrd')
r = requests.post(url="http://210.140.192.189/gapply/manager/html", auth=
auth)
print(r.text)