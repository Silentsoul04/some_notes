mysql主从同步
================
##### 普通文件的数据同步方法: rsync,sersync,scp,nfs,samba,svn

* **nfs 网络文件共享可以同步存储数据**
* **定时任务或守护进程结合rsync,scp**
* **inotify+rsync实时同步**
* ftp 数据同步
* ssh key+scp/rsync
* samba 共享数据

### linux运维场景数据同步方案
##### 文件级别同步方案:
scp,nfs,sftp,http,samba,**rsync**,csync2,union

##### 文件系统级别同步：
* drbd(基于文件系统同步网络raid1),同步几乎任何业务数据
* mysql数据库官方推荐drbd同步数据，所有单点服务例如:nfs,mfs等都可以用drdb

##### 数据库同步方案:
* 自身同步机制
    mysql replication,mysql 主从复制(逻辑的SQL从写)
* 第三方brdb

###mysql主从同步介绍

mysql 支持单项、双向、链式级联、实时、异步复制。在复制过程中，一台服务器充当主服务器(master),而一个或多个其他服务器充当从服务器(slave).

复制可以是单向:M==>S,也可以是双向 M<==>M,当然也可以多M环状同步

如果设置了链式级联复制，那么，从服务器本身除了充当从服务器外，也充当下面从服务器的主服务器 类似于A-B-C-D的复制形式。

#####主从复制应用场景
1、主从服务器互为备份

    主从服务器架构的设置，可以加强数据库架构的健壮性。例如:当主服务器出现问题时，可以人工或自动切换到从服务器继续提供服务。

2、主从服务器读写

    主从服务器架构可通过程序(php,java)或代理软件(mysql-proxy,amoeba)对用户(客户端)的请求实现读写分离，即通过在从服务器上仅仅处理用户的select查询请求，降低用户查询响应事件及读写同时在主服务器带来的压力。更新的数据(update,insert,delete)仍然交给主服务器处理。
    如果网站是以非更新为主(浏览为主)的业务，查询请求较多，这时从服务器读写分离负载均衡策略就很有效了。
    - 中大型网站:通过程序(php,java)
    - 测试环境:代理软件(mysql-proxy,amoeba)
    - 门户网站:分布式dbproxy(读写分离，hash负载均衡,健康检查)

###复制准备:

* 数据库环境准备
    - 具备单机但数据库多实例的环境
    - 或两台以上服务器每台机器一个数据库

* 定义服务器角色
    - 主库:(mysql master): 192.168.58.136 port:3306
    - 从库1:(mysql slava): 192.168.58.136 port:3307
    - 从库2:(mysql slava): 192.168.58.136 port:3308

* 检查主库开启:log-bin,server-id
```bash
egrep "log-bin|server-id" my.cnf
```
    - log-bin,server-id参数都是[mysqld]模块下，否者会出错
    - server-id 的值最好使用ip地址的最后8位如19，目的是避免不同机器或实例ID重复(不适合多实例)
    - 要先再my.cnd配置文件中查找相关参数，并按要求修改,不存在时在添加参数，切记参数不要重复
    - 检查mysql配置后要重启数据库

###配置主从同步
* 主库添加用户从库复制的账号
```sql
grant replication slave on *.* to rep@'192.168.58.%' identified by '123456';
flush privileges;
```
    - replicatiion slave为mysql同步的必须权限,此处不需要授权all

* 在主库上做备份
```sql
flush table with read lock;  #给主库加读锁
show master status; # 查看mysql-bin的点
mysqldump -uroot -p123456 -S /data/3306/mysql.sock -A -B --events  >/opt/rep.sql  #再开一个连接备份mysql 
unlock tables;   #解锁
mysql -uroot -p123456 -S /data/3307/mysql.sock </opt/rep.sql  #导入到从库
```

* 从库执行
```sql
mysql -uroot -p123456 -S /data/3307/mysql.sock

       CHANGE MASTER TO
MASTER_HOST='192.168.58.136',
MASTER_PORT=3306,
MASTER_USER='rep',
MASTER_PASSWORD='123456',
MASTER_LOG_FILE='mysql-bin.000006',
MASTER_LOG_POS=332;

start slave;
```

###mysql主从同步配置步骤
* 1.配置两台数据库环境，或者单台多实例环,能正常启动和登录
* 2.配置my.cnf文件，主库配置bin-log和server-id参数，从库配置serve-id 不能相同。一般从库不开启bin-log功能，重启生效
* 3.登录主库增加用于从库连接主库的账号,并授权replication slave同步的权限
* 4.登录主库，整库锁表flush table with read lock(窗口关闭后失效,超时参数到了也失效)；然后show master status查看binlog的位置状态
* 5.新开窗口,linux命令行备份原有的数据库数据，并拷贝到从库所在服务器目录
* 6.解锁主库 unlock tables;
* 7.把主库导出的原有数据恢复到从库
* 8.根据从库的show master status 查看binlog的位置状态，在从库执行change master to...语句
* 9.从库开启同步开关,start slave
* 10.从库show slave status\G，检查同步状态，并在主库进行更新测试。