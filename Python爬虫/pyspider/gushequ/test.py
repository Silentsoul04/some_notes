# -*- coding:utf8

import MySQLdb

try:
    conn = MySQLdb.connect(host='182.254.226.241',user='gushequ',passwd='gushequ',charset='utf8',port=3306)
    cur = conn.cursor()
    # cur.select_db('mysql')
    conn.select_db('gushequ')
    value = ['20161113','许家印即将第二次举牌万科（20161120）','http://www.zixinke.cn/2016/11/%e8%ae%b8%e5%ae%b6%e5%8d%b0%e5%8d%b3%e5%b0%86%e7%ac%ac%e4%ba%8c%e6%ac%a1%e4%b8%be%e7%89%8c%e4%b8%87%e7%a7%91%ef%bc%8820161120%ef%bc%89/']
    cur.execute("insert into gushequ(date,title,url) values(%s,%s,%s);",value)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print 'Mysql Error Msg:',e