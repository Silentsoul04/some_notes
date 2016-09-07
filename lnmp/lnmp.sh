##mysql5.5
mkdir ~/tools

cd ~/tools
yum -y install cmake ncurses-devel gcc-c++ 

wget http://dev.mysql.com/get/Downloads/MySQL-5.5/mysql-5.5.52.tar.gz

tar zxf mysql-5.5.52.tar.gz && cd mysql-5.5.52

mkdir /application

cmake . -DCMAKE_INSTALL_PREFIX=/application/mysql-5.5.52 \
-DMYSQL_DATADIR=/application/mysql-5.5.52/data \
-DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci \
-DEXTRA_CHARSETS=gbk,gb2312,utf8,ascii \
-DENABLED_LOCAL_INFILE=ON \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_FEDERATED_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 \
-DWITHOUT_PARTITION_STORAGE_ENGINE=1 \
-DWITH_FAST_MUTEXES=1 \
-DWITH_ZLIB=bundled \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_READLINE=1 \
-DWITH_EMBEDDED_SERVER=1 \
-DWITH_DEBUG=0

make && make install

ln -s /application/mysql-5.5.52/ /application/mysql


/bin/cp -rf support-files/my-small.cnf /etc/my.cnf

echo "export PATH=/application/mysql/bin:$PATH" >> /etc/profile
source /etc/profile

useradd -M -s /sbin/nologin mysql

chown -R mysql:mysql /application/mysql/data/

/bin/cp /application/mysql/support-files/mysql.server /etc/init.d/mysqld

cd /application/mysql/scripts/

./mysql_install_db --basedir=/application/mysql/ --datadir=/application/mysql/data/ --user=mysql

/etc/init.d/mysqld start

chkconfig --add mysqld
chkconfig mysqld on

mysqladmin -uroot password "password"

##php5.6
rpm -Uvh http://mirrors.aliyun.com/epel/6/x86_64/epel-release-6-8.noarch.rpm

cd ~/tools
yum install openssl openssl-devel zlib-devel libxml2-devel libjpeg-devel freetype-devel libpng-devel gd-devel curl-devel libmcrypt libmcrypt-devel  mhash-devel mhash libxslt-devel mcrypt -y

wget http://cn2.php.net/get/php-5.6.24.tar.gz

tar zxf php-5.6.24.tar.gz && cd php-5.6.24

./configure --prefix=/application/php-5.6.24  \
--with-mysql=/application/mysql \
--with-iconv-dir=/usr/local/libiconv \
--with-freetype-dir \
--with-jpeg-dir \
--with-png-dir \
--with-zlib \
--with-libxml-dir=/usr/ \
--enable-xml \
--disable-rpath \
--enable-bcmath \
--enable-shmop \
--enable-sysvsem \
--enable-inline-optimization \
--with-curl \
--enable-mbregex \
--enable-fpm \
--enable-mbstring \
--with-mcrypt \
--with-gd \
--with-openssl \
--with-mhash \
--enable-pcntl \
--enable-sockets \
--with-xmlrpc \
--enable-zip \
--enable-soap \
--enable-short-tags \
--enable-static \
--with-xsl \
--with-fpm-user=nginx \
--with-fpm-group=nginx \
--enable-ftp


ln -s /application/mysql/lib/libmysqlclient.so.18 /usr/lib64/

make && make install

ln -s /application/php-5.6.24/ /application/php

/bin/cp php.ini-development /application/php/lib/php.ini
cd /application/php/etc
/bin/cp php-fpm.conf.default php-fpm.conf



##nginx
rpm -Uvh http://nginx.org/packages/mainline/centos/6/x86_64/RPMS/nginx-1.9.8-1.el6.ngx.x86_64.rpm

yum  -y install nginx

