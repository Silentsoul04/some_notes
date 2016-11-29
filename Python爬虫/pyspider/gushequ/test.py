# -*- coding:utf8

import MySQLdb

try:
    conn = MySQLdb.connect(host='119.29.9.37', user='gushequ', passwd='gushequ123', charset='utf8', port=3306)
    cur = conn.cursor()
    # cur.select_db('mysql')
    conn.select_db('gushequ')
    # id,post_author,post_date,post_date_gmt,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,post_password
    # post_name,to_ping,pinged,post_modified,post_modified_gmtpost_content_filtered,post_parent,guid,menu_order
    # post_type,post_mime_type,comment_count
    for i in range(1,498):
        cur.execute("insert into wp_posts(id) values(%s);", i)
        conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print 'Mysql Error Msg:', e


