#-* coding:utf-8 -*-

import requests


user = "hhf1996"
password = "jisilu123"

postdata={"return_url":"https://www.jisilu.cn/","user_name":user,"password":password,"net_auto_login":"1","_post_type":"ajax"}

login_url = "https://www.jisilu.cn/account/ajax/login_process/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

null = "null"
response = requests.post(login_url,data=postdata,headers=headers).content
response_json = eval(response)
if response_json["err"]==null:
    print user + "登录成功.密码为" + password
else:
    print user + "密码不正确."