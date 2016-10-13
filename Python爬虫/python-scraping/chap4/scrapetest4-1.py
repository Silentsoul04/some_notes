import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_ipv4():
    html = urlopen("http://ipinfo.io/ip")
    bsObj = BeautifulSoup(html,"html.parser")
    ipv4 = bsObj.get_text()
    return str(ipv4)
def get_ip_info(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    print("国家代码: " + responseJson.get("country_code"))
    print("经度: " + str(responseJson.get("latitude")))
    print("维度: " + str(responseJson.get("longitude")))

ip = get_ipv4()
print("ip: " + ip)
get_ip_info(ip)