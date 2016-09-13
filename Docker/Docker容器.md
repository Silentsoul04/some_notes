Docker容器
===================

#####概念
容器是Docker的又一核心概念

>简单的说,容器是独立运行的一个或一组应用,以及它们的运行态环境。对应的，虚拟机可以理解为模拟运行的一整套操作系统(提供了运行态环境和其他系统环境)和跑在上面的应用。

本章介绍`如何管理一个容器，包括创建、启动停止等`

####启动容器

启动容器有两种方式

* 基于镜像新建一个容器并启动
* 将在终止状态(stopped)的容器重新启动

由于Docker的容器实在太轻量了，很多用户都是随时删除和新创建容器

#####新建并启动 

命令主要为  `docker run`

```
下面命令输出一个Hello World之后终止容器:
sudo docker run ubuntu:14.04 /bin/echo 'Hello world'

Hello world

这跟在本地直接执行 /bin/echo 'hello world' 几乎感觉不出任何区别。
```
下面的命令则启动一个 bash 终端，允许用户进行交互:
```
sudo docker run -t -i ubuntu:14.04 /bin/bash
root@73627e14833b:/#

-t: 让Docker分配一个伪终端(pseudo-tty)并绑定到容器的标准输入上
-i: 让容器的标准输入保持打开
```
在交互模式下，用户可以通过所创建的终端输入命令

当利用`docker run`来创建容器时,Docker 在后台运行的标准操作包括:
* 检查本地是否存在指定的镜像，不存在就从共有仓库下载
* 利用镜像创建并启动一个容器
* 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
* 从宿主主机配置的网桥接口中桥接一个虚拟接口道容器中去
* 从地址池配置一个ip给容器
* 执行用户指定应用程序
* 执行完毕后容器被终止

#####启动已终止容器

可以利用`docker start`命令,直接将一个已经终止的容器启动运行。

容器的核心为所执行的应用程序，所需要的资源都是应用程序所必需的。除此之外，并没有其他的资源。可以在伪终端查看进程信息。
```
 ps       
   PID TTY          TIME CMD
     1 ?        00:00:00 bash
    16 ?        00:00:00 ps
```
可见，容器中仅运行了指定的 bash 应用。这种特点使得 Docker 对资源的利用率极高，是货真价实的轻量级虚拟化。


#####后台运行

通过添加`-d`参数来实现后台运行 

示例：
```
不加`-d`参数:

sudo docker run ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
容器会把输出的结果(STDOUT)打印到宿主机上面
```
使用`-d`参数
```
sudo docker run -d ubuntu:14.04 /bin/sh -c "while true;do echo hello world;sleep 1;done"

bdc539230993f8718c414371ea6929299d2be2772fddd26b645e2ebe06a4df7e

```

此时容器会在后台运行并不会把输出的结果(STDOUT)打印到宿主机上面(输出结果可以用docker logs 查看)。

注： 容器是否会长久运行，是和docker run指定的命令有关，和 -d 参数无关。

使用 -d 参数启动后会返回一个唯一的 id，也可以通过 docker ps 命令来查看容器信息。
```
docker ps

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
bdc539230993        ubuntu:14.04        "/bin/sh -c 'while tr"   53 seconds ago      Up 51 seconds                           thirsty_rosalind


docker logs bdc539230993
hello world
hello world
hello world
hello world
……………

```

#####终止容器

使用`docker stop`终止一个运行中的容器。

此外,当Docker容器中指定的应用终结时，容器也会自动终止。例如只启动了一个中断的容器，用户通过exit或ctrl+d退出终端时,所创建的容器也会立刻终止。

终止状态的容器可以使用docker ps -a查看。
```
docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                        PORTS               NAMES
bdc539230993        ubuntu:14.04        "/bin/sh -c 'while tr"   4 minutes ago       Exited (0) 2 minutes ago                          thirsty_rosalind
73627e14833b        ubuntu:14.04        "/bin/bash"              56 minutes ago      Exited (127) 22 minutes ago                       agitated_liskov
8d3e2524e4cd        ubuntu:14.04        "/bin/echo 'Hello wor"   58 minutes ago      Exited (0) 58 minutes ago                         ecstatic_joliot
98a5451af1ed        c54a2cc56cbb        "/hello"                 2 hours ago         Exited (0) 2 hours ago                            tiny_franklin
3cb651cf4fbe        fda80281b6a5        "/bin/bash"              4 hours ago         Up 4 hours                                        tender_albattani
f8e859bf39ae        ubuntu:14.04        "/bin/bash"              4 hours ago         Exited (100) 4 hours ago                          condescending_mclean
5c79fa9e1b82        fda80281b6a5        "/bin/bash"              4 hours ago         Exited (127) 4 hours ago                          angry_yonath
59d4cadc1320        fda80281b6a5        "/bin/bash"              4 hours ago         Exited (100) 4 hours ago                          admiring_euler
ae6d751de79a        fda80281b6a5        "/bin/sh -c 'apt-get "   4 hours ago         Exited (100) 4 hours ago                          elated_heisenberg
767863c16727        hhf/ubuntu:v2       "/bin/bash"              4 hours ago         Exited (0) 4 hours ago                            elated_rosalind
4da663bd7268        ubuntu:12.04        "/bin/bash"              4 days ago          Exited (0) 4 days ago                             hopeful_feynman
b42ac8cdd06f        hhf/ubuntu:v2       "/bin/bash"              4 days ago          Exited (1) 5 hours ago                            clever_mccarthy
17e25047c6f9        ubuntu:12.04        "/bin/bash"              4 days ago          Exited (0) 4 days ago                             determined_fermi
0e3c5b1e36a8        nginx:latest        "/bin/bash"              4 days ago          Exited (1) 5 hours ago        80/tcp, 443/tcp     clever_snyder
56042b566449        nginx:latest        "nginx -g 'daemon off"   4 days ago          Exited (0) 4 days ago         80/tcp, 443/tcp     sad_mclean
0a104c75d849        ubuntu:12.04        "/bin/bash"              4 days ago          Exited (0) 4 days ago                             loving_darwin
3838744e86fc        ubuntu:12.04        "/bin/bash"              4 days ago          Exited (0) 4 days ago                             serene_lumiere
720186dd05fb        ubuntu:12.04        "/bin/bash"              4 days ago          Exited (0) 4 days ago                             silly_minsky
883180f49b87        nginx               "nginx -g 'daemon off"   5 days ago          Exited (0) 4 days ago         80/tcp, 443/tcp     some-nginx
9f0459f35230        c54a2cc56cbb        "/hello"                 5 days ago          Exited (0) 5 days ago                             peaceful_dubinsky
884ca9e4c4ed        c54a2cc56cbb        "/hello"                 5 days ago          Exited (0) 5 days ago                             compassionate_payne

```

处于终止状态的容器，可以通过 `docker start` 命令来重新启动。

此外，`docker restart` 命令会将一个运行态的容器终止，然后再重新启动它。

####进入容器

在使用`-d`参数时，容器启动后会进入后台，某些时候需要进入容器进行操作，有很多方法，包括使用`docker attach`命令或者`nsenter`工具等。

#####attach命令

docker attach 是Docker自带的命令。

示例:
```
sudo docker run -idt ubuntu:12.04
8bbeb2400fc8d40f42fbcdd448a29867bef2904e9b62d96e7bef7cc6aebc2b6e

sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
8bbeb2400fc8        ubuntu:12.04        "/bin/bash"         25 seconds ago      Up 24 seconds                           infallible_elion

docker attach 8bbeb2400fc8
```

使用docker attach命令有时候不是很方便。打不过多个窗口同时attche到同一个容器的时候，所有窗口都会同步显示。当某个窗口命令阻塞时，其他窗口也无法执行操作

##### nsenter命令 

nsenter 工具在 util-linux 包2.23版本后包含。 如果系统中 util-linux 包没有该命令，可以按照下面的方法从源码安装。

```
cd /tmp; curl https://www.kernel.org/pub/linux/utils/util-linux/v2.24/util-linux-2.24.tar.gz | tar -zxf-; cd util-linux-2.24;
./configure --without-ncurses
make nsenter && sudo cp nsenter /usr/local/bin
```

为了连接到容器，你还需要找到容器的第一个进程的 PID，可以通过下面的命令获取。
```
PID=$(docker inspect --format "{{ .State.Pid }}" <container>)
```

通过这个 PID，就可以连接到这个容器：
```
$ nsenter --target $PID --mount --uts --ipc --net --pid
```

完整的:
```
sudo docker run -idt ubuntu:12.04
89d49c3a1b9551077377e3f9706c51269a65bab411335a0107b437be413e7075

sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
89d49c3a1b95        ubuntu:12.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           evil_saha

PID=$(docker-pid 89d49c3a1b95)

sudo nsenter --target $PID --mount --uts --ipc --net --pid

```

更简单的，可以下载 [.bashrc_docker](https://raw.githubusercontent.com/yeasy/docker_practice/master/_local/.bashrc_docker)，并将内容放到 .bashrc 中。
```
wget -P ~ https://github.com/yeasy/docker_practice/raw/master/_local/.bashrc_docker;

echo "[ -f ~/.bashrc_docker ] && . ~/.bashrc_docker" >> ~/.bashrc; source ~/.bashrc
```
这个文件中定义了很多方便使用 Docker 的命令，例如 docker-pid 可以获取某个容器的 PID；而 docker-enter 可以进入容器或直接在容器内执行命令。


####导入与导出容器

#####导出

导出容器可以使用`docker export`
```
docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                       PORTS               NAMES
89d49c3a1b95        ubuntu:12.04        "/bin/bash"              12 hours ago        Exited (137) 2 minutes ago                       evil_saha

sudo docker export 89d49c3a1b95 > ubuntu_export.tar
```
#####导入:
```
cat ubuntu_export.tar | docker import - test/ubuntu:v1.0
```
此外也可以从指定url导入,例如:

```
sudo docker import http://example.com/exampleimage.tgz example/imagerepo
```
note:
>用户既可以使用`docker load`来导入镜像存储文件到本地镜像库，也可以使用`docker import` 导入一个容器快照到本地镜像库，这两者的区别在于容器快照文件将丢弃所有的历史记录和元数据信息(仅保存容器当时的快照状态)，而镜像文件将保存完整记录，体积也要大。此外，从容器快照文件导入时可以指定标签等元数据信息

#####删除容器:

可以使用`docker rm`删除已终止的容器
```
docker rm 884ca9e4c4ed
docker rm peaceful_dubinsky

884ca9e4c4ed为容器id,peaceful_dubinsky为names
```


#####清理所有处于终止状态的容器

用 `docker ps -a` 命令可以查看所有已经创建的包括终止状态的容器，如果数量太多要一个个删除可能会很麻烦，用 `docker rm $(docker ps -a -q)` 可以全部清理掉。

**注意：这个命令其试图删除所有的包括还在运行中的容器，不过docker rm默认并不会删除运行中的容器。**

