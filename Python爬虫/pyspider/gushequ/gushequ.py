import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"}

articleUrl = "http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MjAxNTE4MA==#wechat_webview_type=1&wechat_redirect"

session = requests.session()
allArticle = session.get(articleUrl)
print allArticle.text