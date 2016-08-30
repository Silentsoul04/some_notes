#####ssh密钥对
```bash
ssh-keygen -t rsa -C "853885165@qq.com"
cat ~/.ssh/id_rsa.pub
```
将密钥对放到github上。

#####添加远程库
github上创建远程仓库: [git_test](https://github.com/lovehhf/git_test)
        
    git remote add origin https://github.com/lovehhf/git_test xxxxoooo 不能用
    or
    git remote add origin  git@github.com:lovehhf/git_test 

提示:
    
    fatal: remote origin already exists.

解决:
    
    git remote rm origin

把本地库的所有内容同步到远程库上:

    git push -u origin master

报错提示:TAT一脸懵逼
```
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/lovehhf/git_test/info/refs

fatal: HTTP request failed
```
解决
```
vi .git/config
修改:
[remote "origin"]
        url = https://github.com/lovehhf/git_test
为
[remote "origin"]
        url = git@github.com:lovehhf/git_test
```
原因是git add的时候用错url了，不该装逼。。。
```
Counting objects: 22, done.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (21/21), 1.44 KiB, done.
Total 21 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), done.
To git@github.com:lovehhf/git_test
   cf5358f..edfb16b  master -> master
Branch master set up to track remote branch master from origin.
```
远程库步骤小结:

* git remote add origin git@github.com:/../..
* git add 添加文件
* git commit 添加到版本库
* git push -u origin master 推送到远程库
* git pull 与远程库同步

#####从远处库克隆
```
git clone https://github.com/lovehhf/git_test
```

    git支持多种协议，包括https，但通过ssh支持的原生git协议速度最快。

