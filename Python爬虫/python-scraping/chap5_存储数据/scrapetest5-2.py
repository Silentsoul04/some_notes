from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import os

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteUrl(baseUrl,source):
    if (source.startswith("http://www.")):
        url = "http://" + source[11:]
    elif (source.startswith("http://")):
        url = source
    elif source.startswith("www."):
        url = "http://"+source[4:]
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(e)
    return path

url = "http://www.pythonscraping.com/"
html = urlopen(url)
bsObj = BeautifulSoup(html,"html.parser")
downloadList = bsObj.find_all(src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        try:
            urlretrieve(fileUrl,getDownloadPath(baseUrl, fileUrl, downloadDirectory))
        except OSError as e:
            print(e)