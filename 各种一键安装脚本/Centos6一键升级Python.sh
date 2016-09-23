#! /bin/bash 

function pre_install(){
	yum -y update
	yum groupinstall -y 'development tools'
	yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget readline-devel.*
}

function compile_python(){
	cd ~
	wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
	tar zxf Python-2.7.12.tgz
	cd Python-2.7.12
	./configure --prefix=/usr/local
	make && make altinstall
}

function soft_links(){
	rm /usr/bin/python
	ln -s /usr/local/bin/python2.7  /usr/bin/python
}

function install_pip(){
	curl  https://bootstrap.pypa.io/get-pip.py | python2.7 -
}

function fix_error(){
	sed -i  '1s#.*#\#!/usr/bin/python2.6#g' /usr/bin/yum
}



pre_install
compile_python
soft_links
install_pip
fix_error