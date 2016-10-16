import requests



"""
向欢迎页面发送了一个登录参数，它的作用就像登录表单的处理器。然后我从请求
结果中获取 cookie，打印登录状态的验证结果，然后再通过 cookies 参数把 cookie 发送到
简介页面。
"""

params = {'username': 'Ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("----------------------------------------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
print(r.text)