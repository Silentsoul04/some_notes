##### 获取镜像
可以使用`docker pull`命令从仓库获取所需要的镜像
```
eg: 从Docker hub仓库下载一个ubuntu12.04操作系统的镜像:
sudo docker pull ubuntu:12.04


```

`docker pull ubuntu:12.04`命令实际相当于`docker pull registry.hub.docker.com/ubuntu:12.04`命令,即从注册服务器 `istry.hub.docker.com`中的`ubuntu`仓库下载标记为12.04的镜像。

有时候官方仓库注册服务器下载较慢，可以从其他仓库下载。 从其它仓库下载时需要指定完整的仓库注册服务器地址。

完成后,即可随时使用该镜像了,例如创建一个容器,让其运行bash应用。
```
sudo docker run -t -i ubuntu:12.04 /bin/bash
root@720186dd05fb:/
```

#####列出本地镜像:
```
sudo docker images

[root@hhf ~]# sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              12.04               a11493a01736        12 days ago         103.6 MB
nginx               latest              4efb2fcdb1ab        2 weeks ago         183.4 MB
hello-world         latest              c54a2cc56cbb        9 weeks ago         1.848 kB
```
列出的字段信息:
* 来自哪个仓库 eg:ubuntu
* 镜像标记 eg: 12.04
* ID号(唯一) eg: a11493a01736
* 创建时间
* 镜像大小

>注:镜像的ID唯一标记了镜像，TAG信息用来标记同一仓库的不同镜像 ,例如`ubuntu`仓库有多个镜像，通过TAG信息来区分发行版本,例如12.04,14.04,16.04等。例如下面的命令指定使用镜像ubuntu: 12.04来启动一个容器

```
sudo docker run -t -i ubuntu:12.04 /bin/bash
```
