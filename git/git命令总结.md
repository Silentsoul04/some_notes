#####安装
ubuntu/debain:
```bash
    apt-get install git
```
redhat/centos:
```bash
    yum install git
```

#####简单配置

```git
git config --global user.name "lovehhf"
git config --global user.email "853885165@qq.com"
```

#####初始化
```bash
mkdir git_test&&cd git_test
git init
```
创建一个readme.md文件:
```bash
cat >>readme.md<<EOF
git is a version syetem.
git is free soft
EOF
```
添加文件readme.md到git
```bash
git add readme.txt
```
    
    执行上面的命令，没有任何显示，这就对了，Unix的哲学是“没有消息就是好消息”，说明添加成功。

用命令git commit告诉Git，把文件提交到仓库：
```bash
git commit -m "add readme.md"
```

    -m是本次提交的说明，可以输入任何内容，当然最好都是有意义的

当然也可以同时提交多个文件
```bash
for i in `seq 10`;do echo "file${i}.txt" >>file${i}.txt;done
git add file{1..10}
git commit -m "add 10 files"
```

####时空机穿梭

此时修改readme.md

    Git is a distributed version control system.
    Git is free software.

运行git status命令查看结果:

    # On branch master
    # Your branch is ahead of 'origin/master' by 1 commit.
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #   readme.md
    nothing added to commit but untracked files present (use "git add" to track)

git diff查看修改的内容:

    git diff readme.md

    diff --git a/readme.md b/readme.md
    index 7bdb4a3..1689320 100644
    --- a/readme.md
    +++ b/readme.md
    @@ -1,2 +1,2 @@
    -**Git is a version control system.**
    +**Git is a distributed version control system.**
     **Git is free software.**

再次commit后git status查看仓库当前状态:
```
 git add readme.md 
 git commit -m "change readme.md"
 git status

# On branch master
# Your branch is ahead of 'origin/master' by 3 commits.
#
nothing to commit (working directory clean)
```

#####版本回退
再次修改readme.md 

    Git is a distributed version control system.
    Git is free software distributed under the GPL.

    git add readme.txt
    git commit -m "append GPL"

现在有readme.md有三个版本:
``` 
版本一:(add readme.md)
Git is a version control system.
Git is free software.
版本二:(change readme.md)
Git is a distributed version control system.
Git is free software.
版本三:(append GPL)
Git is a distributed version control system.
Git is free software distributed under the GPL.
```

git log查看修改的历史记录
```
git log:

commit edfb16b762556f54296001369b8229d2a85fa31d
Author: lovehhf <853885165@qq.com>
Date:   Mon Aug 29 19:50:26 2016 +0800

    addend GPL

commit 318d59aa0b053bf1eac482d34bf5f7da6c862ff9
Author: lovehhf <853885165@qq.com>
Date:   Mon Aug 29 19:46:59 2016 +0800

    change readme.md

commit a9322ea132e73ce790ec24653c5dfa266d574370
Author: lovehhf <853885165@qq.com>
Date:   Mon Aug 29 19:41:32 2016 +0800

    add readme.md
```

git log命令显示从最近到最远的提交日志,如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数：

```
    git log --pretty=oneline

    edfb16b762556f54296001369b8229d2a85fa31d addend GPL
    318d59aa0b053bf1eac482d34bf5f7da6c862ff9 change readme.md
    a9322ea132e73ce790ec24653c5dfa266d574370 add readme.md
    60877474ee1e31d5e99cdcbbbba4992e2a4ad835 add 10 files
    cf5358fbe28514ff886c3f06e91cc534f01e7e3b add abc
```

要回退到上一个版本，也就是"change readme.md"版本。

首先，Git必须知道当前版本是哪个版本，在Git中，用HEAD表示当前版本，也就是最新的提交edfb16b762556f54296001369b8229d2a85fa31d，上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。

要回退到上一个版本“change readme.md”，可以使用git reset命令:
```
    git reset --hard HEAD^

    HEAD is now at 318d59a change readme.md
```

此时append GPL已经看不到了！如果需要回到append GPL那还的往回找到哪个commit id:edfb16...，于是就能指定回到那个未来的版本

    git reset --hard edfb16
    HEAD is now at edfb16b addend GPL

版本号没必要写全，前几位就可以了，git会自动去找。当然也不能只写前面一两位，因为git可能会找到很多个版本号，就无法确定是哪一个了

Git的版本回退速度非常快，因为Git在内部有个指向当前版本的HEAD指针，当你回退版本的时候，Git仅仅是把HEAD从指向append GPL,改为指向add distributed。

如果找不到commit id怎么办?
当你用`$ git reset --hard HEAD^`回退到`add distributed`版本时，再想恢复到append GPL，就必须找到append GPL的commit id。Git提供了一个命令`git reflog`用来记录你的每一次命令：
```bash
git reflog
318d59a HEAD@{0}: HEAD^: updating HEAD
edfb16b HEAD@{1}: edfb16: updating HEAD
318d59a HEAD@{2}: HEAD^: updating HEAD
edfb16b HEAD@{3}: commit: addend GPL
318d59a HEAD@{4}: commit: change readme.md
a9322ea HEAD@{5}: commit: add readme.md
6087747 HEAD@{6}: commit: add 10 files
```

#####工作区与暂存区
工作区:能看到的目录
暂存区：.git里面，是git的版本库。

    Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。


#####撤销修改
修改文件后使用 git checkout -- file 可以丢弃工作区的修改
例如：
修改readme.md的文件后，使用 git checkout -- readme.md 可以撤销对其的修改git checkout -- file 还能被rm删除的文件

#####删除文件
普通的rm不会记录到版本库中，无法commit。

git rm 用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删。但是要小心，你只能恢复文件到最新版本，你会丢失**最近一次提交后你修改的内容**。