##### 介绍

>GitLab是一个利用Ruby on Rails开发的开源应用程序，实现一个自托管的Git项目仓库，可通过Web界面进行访问公开的或者私人项目。

>它拥有与GitHub类似的功能，能够浏览源代码，管理缺陷和注释。可以管理团队对仓库的访问，它非常易于浏览提交过的版本并提供一个文件历史库。团队成员可以利用内置的简单聊天程序（Wall）进行交流。它还提供一个代码片段收集功能可以轻松实现代码复用，便于日后有需要的时候进行查找。

>GitLab要求服务器端采用Gitolite搭建（为了方便安装，现已经用gitlab-shell代替Gitolite）。

---摘自[wikipedia](https://zh.wikipedia.org/wiki/Gitlab)


##### 准备: 

* centos6 服务器一台

##### 开始: 
1.添加gitlab-ce.repo

```bash 
cat > /etc/yum.repos.d/gitlab-ce.repo << EOF
[gitlab-ce]
name=gitlab-ce
baseurl=http://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el6
repo_gpgcheck=0
gpgcheck=0
enabled=1
gpgkey=https://packages.gitlab.com/gpg.key
EOF
```

2.验证repo文件是否起效
```bash
yum list|grep gitlab-ce
```

3.安装gitlab-ce
```bash
sudo yum makecache
sudo yum install gitlab-ce
```

4.配置并启动gitlab

```bash
sudo gitlab-ctl reconfigure
```

5.安装完成后可以通过`http://ip`访问了gitlab,默认账户是root，首次登录会设置更改密码。

6.配置文件在`/etc/gitlab/gitlab.rb`可根据需要更改，每次更改`gitlab.rb`都需要重新运行
```bash
sudo gitlab-ctl reconfigure
```

##### 其他
* 其他版本linux安装参考
    - [Gitlab Community Edition 镜像使用帮助](https://mirror.tuna.tsinghua.edu.cn/help/gitlab-ce/)
    - [Download GitLab Community Edition (CE)](https://about.gitlab.com/downloads/#centos6)

* git使用参考:
    - [Git教程 廖雪峰](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
    - [猴子都能懂的GIT入门](http://backlogtool.com/git-guide/cn/intro/intro1_1.html)
    - [Pro Git](https://git-scm.com/book/zh/v2)