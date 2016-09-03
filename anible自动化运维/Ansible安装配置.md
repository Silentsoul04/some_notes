
#####准备

* 从哪里获取安装软件包
    - Github:[github.com/ansible/ansible](https://github.com/ansible/ansible)
* 需要安装那些支持软件
    - 不需要安装支撑软件
* 安装哪个版本的软件
* 控制主机需要准备哪些条件
    - Python 2.6或以上 2.7最佳
    - paramiko模块
    - PyYAML
    - Jinja2
    - httplib2
* 被管节点需要准备哪些条件

* 关于python版本
    - 如果一些Linux 发行版默认没有安装Python2.x,需要安装Python2.x解释器，并把资源清单(inventory)中的ansible_python_interpreter变量设置为Python2.x。也可以使用raw模块在被管节点上远程安装Python2.x

#####安装
使用源码安装

 * 从git源码库获取源码

```
    1. git clone https://github.com/ansible/ansible
    2. cd ./ansible
    3. source ./hacking/env-setup ##如果想要在安装过程中没有警告，使用-q参数 source ./hacking/env-setup-q
    4. pip install paramiko PyYAML Jinja2 httplib2 six
    当更新ansible版本时，不但要更新git的源码树，还要更新Ansible自身的模块，称为submodules:
        git pull --rebase
        git submoudle update --init --recursive
    一旦运行env-setup脚本，就意味着Ansible从源码中运行起来了。默认的inventory是/etc/ansible/host
```

* tar包安装方式
* 制作rpm包(也需要解决依赖问题)

```
   43  git clone https://github.com/ansible/ansible
   46  cd ansible/
   54  git checkout v1.9.4-1
   55  git branch
   56  yum -y install rpm-build make python2-devel   ****
   57  make rpm
   60  yum -y install python-pip
   61  make rpm
   62  ls
   63  cd ~
   64  ls
   65  cd ansible/
   66  ls
   67  rpm -Uvh ./rpm-build/ansible-*.noarch.rpm   ###会提示需要哪些依赖
   68   pip install paramiko PyYAML Jinja2 httplib2 six
   69  rpm -Uvh ./rpm-build/ansible-*.noarch.rpm
   70  yum install sshpass
   71  rpm -Uvh ./rpm-build/ansible-*.noarch.rpm
   72  pip install PyYAML crypto2.6 httplib2 jinja2 keyczar
   73  pip install PyYAML crypto httplib2 jinja2 keyczar
   74  yum install python-keyczar
   75  rpm -Uvh ./rpm-build/ansible-*.noarch.rpm
   76  yum install PyYAML python-crypto2.6 python-httplib2 python-jinja2 *****
   77  rpm -Uvh ./rpm-build/ansible-*.noarch.rpm
```




用包管理工具安装

* yum 安装(centos6)
    使用aliyun的epel源作为部署ansible的默认源    rpm -Uvh http://mirrors.aliyun.com/epel/6/x86_64/epel-release-6-8.noarch.rpm
    yum install ansible
* apt(ubuntu)
```
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```
* Homebrew(mac)
```
brew update
brew install ansible
```
* pip:
```
pip install ansible
```

#####配置运行环境

>Ansible配置文件是以ini格式存储配置数据的，Ansible中，几乎所有的配置项都可以通过Ansible的playbook环境重新复制，运行Ansible命令时，命令会先按照预先设定的顺序查找配置文件，顺序如下:

1. ANSIBLE_CONFIG: 首先 Ansible命令会检查环境变量，及这个环境变量指向的配置文件
2. `./ansible.cfg` 其次，将检查当前目录下的ansible.cfg配置文件
3. `~/.ansible.cfg` 然后,会检查当前用户家目录的.ansible.cfg配置文件
4. `/etc/ansible/ansible.cfg`最后会检查软件包管理工具安装Ansible目录自动生成的配置文件
    - 如果是包管理工具安装的,会自动生成`/etc/ansible`，源码编译的可以复制example目录下找到ansible.cfg

`ansible.cfg`参数配置：
```
inventory = /etc/host
libary = /usr/share/ansible      
    # libary就是存放Ansible模块的目录，Ansible支持多个目录方式，需用:隔开
fork = 5 
    # 默认最多能有5个进程同时工作，可以根据主机性能和被管节点数量自己设置
sudo_user = root
    # 这是设置默认执行命令的用户，也可再playbook重新设置这个参数
remote_port = 22 
    # 设置ssh端口，默认22
host_key_checking = False
    # 是个检查SSH主机的密钥,bool值
timeout = 60
    # 设置ssh连接超时时间，默认60秒
log_path = /var/log/ansible.log
    # Ansible 系统默认是不记录日志的，如果要把Ansible系统的输出记录到日志文件中，需要知之间一个存储Ansible日志的文件，另外执行Ansible的用户需要有写入日志的权限，模块会调用被管节点的sys-log来记录，口令不会出现在日志中
```



#####获取帮助
```
ansible-doc 
    -h    # 查看ansible-doc的帮助  --help
    -l    # 列出可用的命令  --list
    -s    # 列出指定模块的用法
    -M    # q
```