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

