import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

"""
处理HTTP 接入验证
"""

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=
auth)
print(r.text)