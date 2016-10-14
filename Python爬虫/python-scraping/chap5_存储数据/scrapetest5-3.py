from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='182.254.226.241',user='hhf',passwd='hhf960214',db='hhf')

cur = conn.cursor()

cur.execute("show tables;")
result = cur.fetchone()
print(result)
cur.close()
conn.close()