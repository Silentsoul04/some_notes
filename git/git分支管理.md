分支作用:

    假设你准备开发一个新功能，但是需要两周才能完成，第一周你写了50%的代码，如果立刻提交，由于代码还没写完，不完整的代码库会导致别人不能干活了。如果等代码全部写完再一次提交，又存在丢失每天进度的巨大风险。

创建dev分支，然后切换到dev分支：
```
git checkout -b dev

相当于:
git branch dev
git checkout dev
```

查看当前分支:
```
git branch
* dev
  master

git branch命令会列出所有分支，当前分支前面会标一个*号
```

然后，可以对dev分支正常提交,比如对readme.md做个更改。加上一行
```
Creating a new branch is quick.
```
然后提交:
```
git add readme.md
git commit -m "branch test"
git push -u origin dev
```
切换回master查看会发现刚才的修改的内容不见了，因为那个提交是在dev分支上，而master分支此刻的提交点并没有变：
```
git checkout master
```
现在，把dev分支的工作成果合并到master上:
```
git merge dev

Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.
```

    git merge命令用于合并指定分支到当前分支。合并后，再查看readme.txt的内容，就可以看到，和dev分支的最新提交是完全一样的。

合并完成后，就可以放心地删除dev分支了：
```
git merge dev

Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.
[root@hhf git_test]# git branch -d dev
warning: deleting branch 'dev' that has been merged to
         'refs/remotes/origin/dev', but it is not yet merged to HEAD.
Deleted branch dev (was 3f1a974).
```
因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在master分支上工作效果是一样的，但过程更安全。

删除github上的分支：
```
git push origin :dev
To git@github.com:lovehhf/git_test
 - [deleted]         dev
```

再次提示创建分支提示:
```
git checkout -b branch1

readme.md: needs merge
error: you need to resolve your current index first
```
解决: [Git merge errors](http://stackoverflow.com/questions/6006737/git-merge-errors)

git reset --merge

小结:

* Git鼓励大量使用分支：
* 查看分支：git branch
* 创建分支：git branch <name>
* 切换分支：git checkout <name>
* 创建+切换分支：git checkout -b <name>
* 合并某分支到当前分支：git merge <name>
* 删除分支：git branch -d <name>

####解决分支冲突:

新建branch2分支：
```
git checkout -b branch2
```
修改readme.md添加一行hehe.

    git add readme.md 
    git commit -m "hehe"
切换到master分支添加 haha,提交到版本库
```bash
git merge branch2

Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.
```

Git告诉我们，readme.md文件存在冲突，必须手动解决冲突后再提交。git status也可以告诉我们冲突的文件：
```
# On branch master
# Your branch is ahead of 'origin/master' by 3 commits.
#
# Unmerged paths:
#   (use "git add/rm <file>..." as appropriate to mark resolution)
#
#   both modified:      readme.md
#
no changes added to commit (use "git add" and/or "git commit -a")

```

查看readme 文件:
```
**Git is a distributed version control system.**

**Git is free software under the GPL..**

**Creating a new branch is quick.**

>test branch

    hehe
<<<<<<< HEAD
=======

[晨飞小窝](http://www.ichenfei.com)

>>>>>>> branch2
>haha
```
    Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容，我们修改如下后保存：

再提交
```
 git add readme.md
 git commit -m "conflict fixed"
```
用带参数的git log可以查看分支合并情况
```
git log --graph --pretty=oneline --abbrev-commit
*   cd574f2 conflict fixed
|\  
| * 6515731 test conflict
* | c5dabbd haha test conflict
|/  
```

#####分支管理策略

合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。

如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。

合并分支使用--no-ff参数表示禁用Fast forward

    git merge --no-ff -m "merge with no-ff" branch

#####Bug分支
#####feature分支

#####多人协作的工作模式:

* 1.首先，可以试图用git push origin branch-name推送自己的修改；
* 2.如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
* 3.如果合并有冲突，则解决冲突，并在本地提交；
* 4.没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！


小结

* 查看远程库信息，使用git remote -v；
* 本地新建的分支如果不推送到远程，对其他人就是不可见的；
* 从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；
* 在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
* 建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
*　从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。