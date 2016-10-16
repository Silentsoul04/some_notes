import requests

"""
在这个例子中，会话（session）对象（调用 requests.Session() 获取）会持续跟踪会话信
息，像 cookie、header，甚至包括运行 HTTP 协议的信息，比如 HTTPAdapter（为 HTTP
和 HTTPS 的链接会话提供统一接口）。
"""

session = requests.Session()

params = {'username': 'Ryan', 'password': 'password'}
req = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)

print("Cookie is set to: " + str(req.cookies.get_dict()))

print("----------------------------------------")
print("Going to profile page...")

s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)