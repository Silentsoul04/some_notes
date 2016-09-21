CentOS 6 自带的python版本是 2.6 , 然而很多时候都需要python 2.7。所以需要进行版本升级。另外由于一些系统工具和服务是对 Python 有依赖的，所以升级 Python 版本需要注意。

#####升级步骤如下

1.安装编译python源码的一些必要工具
```
yum -y update
yum groupinstall -y 'development tools'
yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget readline-devel.*
```
2.下载python2.7源码
```
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
tar zxf Python-2.7.12.tgz 
cd Python-2.7.12
./configure --prefix=/usr/local
make && make altinstall
```
3.建立软链接
```
rm /usr/bin/python
ln -s /usr/local/bin/python2.7  /usr/bin/python
```
4.安装pip
```
curl  https://bootstrap.pypa.io/get-pip.py | python2.7 -
```
5.修复 yum
```
vim /usr/bin/yum
将第一行  #!/usr/bin/python  改为 #!/usr/bin/python2.6
```