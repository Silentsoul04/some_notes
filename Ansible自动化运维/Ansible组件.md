#####Inventory
* Inventory
    - 定义主机和主机组:
```
10.0.0.4 ansible_ssh_pass='123456'
10.0.0.5 ansible_ssh_pass='123456'
[docker]
10.0.0.[4:6]
[docker:vars]
ansible_ssh_pass='123456'
[ansible:children]
docker
```
    - 多个Inventory列表
    - 动态Inventory

* Inventory内置参数
```
ansible_ssh_host      定义hosts ssh地址  ansible_ssh_host=10.0.0.117
ansible_ssh_port      定义hosts ssh端口  ansible_ssh_port=5000
ansible_ssh_user      定义hosts ssh认证用户 ansible_ssh_user=root
ansible_ssh_password  定义hosts ssh认证密码  ansible_ssh_pass='123456'
ansible_sudo          定义hosts sudo 用户  ansible_sudo=huanghongfei
ansible_sudo_pass     定义hosts sudo 密码  ansible_sudo_pass='123456'
ansible_sudo_exe      定义ansible sudo路径 ansible_sudo_exe=/usr/bin/sudo
ansible_connection    定义hosts连接方式  ansible_connection=local
ansible_ssh_private_key_file  定义hosts私钥 ansible_ssh_private_key_file=/root/key
ansible_shell_type    定义hosts shell类型 ansible_shell_type=zsh
ansible_python_interpreter  定义hosts任务执行的python路径 ansible_python_interpreter=/usr/bin/python2.6
ansible_*_interpreter       定义hosts其他语言解释器路径 ansible_ruby_interpreter=/usr/bin/ruby
```

#####Ansible Ad-Hoc命令

* 执行命令
```
ansible all -m command -a "hostname" -o 

10.0.0.5 | SUCCESS | rc=0 | (stdout) hhf
10.0.0.4 | SUCCESS | rc=0 | (stdout) hhf
10.0.0.6 | SUCCESS | rc=0 | (stdout) hhf
```
* 复制文件
```
ansible docker -m copy -a 'src=test.txt dest=/root/test.txt owner=root group=root mode=644 backup=yes' -o

10.0.0.5 | SUCCESS => {"changed": true, "checksum": "319e4e50d3af0948f75667eb6eea7a5ea59ead3e", "dest": "/root/test.txt", "gid": 0, "group": "root", "md5sum": "10a4c570125b8844496864febbb69c20", "mode": "0644", "owner": "root", "size": 31, "src": "/root/.ansible/tmp/ansible-tmp-1472804259.28-58296059610044/source", "state": "file", "uid": 0}
10.0.0.6 | SUCCESS => {"changed": true, "checksum": "319e4e50d3af0948f75667eb6eea7a5ea59ead3e", "dest": "/root/test.txt", "gid": 0, "group": "root", "md5sum": "10a4c570125b8844496864febbb69c20", "mode": "0644", "owner": "root", "secontext": "system_u:object_r:admin_home_t:s0", "size": 31, "src": "/root/.ansible/tmp/ansible-tmp-1472804272.15-256270838711530/source", "state": "file", "uid": 0}
10.0.0.4 | SUCCESS => {"changed": false, "checksum": "319e4e50d3af0948f75667eb6eea7a5ea59ead3e", "dest": "/root/test.txt", "gid": 0, "group": "root", "mode": "0644", "owner": "root", "path": "/root/test.txt", "secontext": "unconfined_u:object_r:admin_home_t:s0", "size": 31, "state": "file", "uid": 0}

验证文件下发功能:
ansible docker -m shell -a 'md5sum /root/test.txt' -f 5 -o
10.0.0.5 | SUCCESS | rc=0 | (stdout) 10a4c570125b8844496864febbb69c20  /root/test.txt
10.0.0.4 | SUCCESS | rc=0 | (stdout) 10a4c570125b8844496864febbb69c20  /root/test.txt
10.0.0.6 | SUCCESS | rc=0 | (stdout) 10a4c570125b8844496864febbb69c20  /root/test.txt
```
* 包和服务管理
```
ansible docker -m yum -a 'name=httpd state=latest' -f 5 -o

10.0.0.5 | SUCCESS => {"changed": false, "msg": "", "rc": 0, "results": ["All packages providing httpd are up to date", ""]}
10.0.0.4 | SUCCESS => {"changed": false, "msg": "", "rc": 0, "results": ["All packages providing httpd are up to date", ""]}
10.0.0.6 | SUCCESS => {"changed": false, "msg": "", "rc": 0, "results": ["All packages providing httpd are up to date", ""]}

ansible docker -m service -a 'name=httpd state=started' -f 5 -o

10.0.0.5 | SUCCESS => {"changed": false, "name": "httpd", "state": "started"}
10.0.0.6 | SUCCESS => {"changed": true, "name": "httpd", "state": "started"}
10.0.0.4 | SUCCESS => {"changed": true, "name": "httpd", "state": "started"}

ansible docker -m shell -a 'rpm -qa httpd' -f 5 -o
10.0.0.6 | SUCCESS | rc=0 | (stdout) httpd-2.2.15-54.el6.centos.x86_64
10.0.0.5 | SUCCESS | rc=0 | (stdout) httpd-2.2.15-54.el6.centos.x86_64
10.0.0.4 | SUCCESS | rc=0 | (stdout) httpd-2.2.15-54.el6.centos.x86_64
```

* Ansible playbook
    - Ansible 非常非常重要的组件之一

* Ansible facts
    - facts是Ansible用于采集被管理极其设备信息的一个功能,使用setup模块查机器的所有facts信息，可以使用filter来指定信息。整个facts信息被包括在一个JSON格式的数据结构中,ansible_facts 是最上层的值。 
```
ansible docker -m setup

一大堆输出......

ansible 10.0.0.5 -m setup -a 'filter=ansible_all_ipv4_addresses'
10.0.0.5 | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "10.0.0.5"
        ]
    }, 
    "changed": false
}

```

* Ansible role
     role只是对日常使用的playbook的目录结构进行一些规范,与playbook没什么区别
* Ansible Galaxy
    - ansible-galaxy install 默认会安装到/etc/ansible/role/目录下，其引用跟自己写的role引用方式是一样的