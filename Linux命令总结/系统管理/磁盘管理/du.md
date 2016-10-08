du(disk usage)
=================

* 功能说明: 显示某个指定某个特定目录(默认是当前目录)的磁盘使用情况
    - 判断某个目录是不是有超大文件

默认情况下,du命令会显示当前目录下所有文件、目录和子目录的使用情况，它以磁盘的块为单位来显示每个文件或目录占用了多大存储，在标准的主目录中，这个输出会是个比较长的列表。

* 命令格式:

```
du [选项] [文件]
```

* 命令参数:
    - `-h` 以人类可读形式展示。`--human-readable`
    - `-H` 与`-h`相同，但是计算是，1K=1000，而不是1K=1024
    - `-m` 以MB为单位输出。   
    - `-k` 以KB(1024bytes)为单位输出。
    - `-a` 统计所有文件大小,默认只显示目录
    - `-s` 显示每个出书的参数的总计 `--summarize`
    - `-c` 除了显示个别目录或文件的大小外，同时也显示所有目录或文件的总和。 

* 使用示例:


```
[root@localhost ~]# du

936     ./Parser
640     ./Include
5272    ./Python
136     ./PC/os2emx
212     ./PC/VC6
244     ./PC/os2vacpp
436     ./PC/VS7.1
172     ./PC/bdist_wininst
528     ./PC/VS8.0
576     ./PC/VS9.0
2640    ./PC
………………
126272  .

每行输出开始地方的数值,是每个文件或目录占用的磁盘块数。这个列表是从目录最底层开始的，然后按文件，子目录，目录逐级向上。

[root@localhost ~]# du -h Python-2.7.12.tgz 
17M Python-2.7.12.tgz

[root@localhost ~]# du -sh
158M    .

[root@localhost ~]# du -sh Python-2.7.12 ipvsadm-1.26
124M    Python-2.7.12
680K    ipvsadm-1.26

[root@localhost ~]# du -ch ipvsadm-1.26.tar.gz Python-2.7.12.tgz 
44K ipvsadm-1.26.tar.gz
17M Python-2.7.12.tgz
17M total


```
