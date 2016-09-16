Docker使用网络
==================
>Docker 允许通过外部访问容器或容器互联的方式来提供网络服务。

###外部访问容器

容器中可以运行一些网络应用，要让外部可以访问这些应用，可以通过`-P`或`-p`参数指定端口映射。

当使用-P标记时，Docker会随机映射一个端口到内部容器开发的网络端口。
使用`docker ps`可以看到，本地主机的32773映射到了容器的80端口，此时访问本机的32771端口即可访问容器内web应用提供的界面。
```
docker run -d -P nginx
daed4fe4d75b436e4e34092adfda1f44ec5c0b535b48b010d8e2d4f37d07c277


 docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                                           NAMES
daed4fe4d75b        nginx               "nginx -g 'daemon off"   10 seconds ago       Up 9 seconds        0.0.0.0:32773->80/tcp, 0.0.0.0:32772->443/tcp   stupefied_poincare
```
同样的，可以通过 `docker logs`命令来查看应用的信息。

-p可以指定要映射的端口，并且，在一个指定端口上只可以绑定一个容器。支持的格式有 `ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort。`


#####映射所有接口地址

使用 `hostPort:containerPort` 格式本地的 8080 端口映射到容器的 80 端口，可以执行
```
 docker run -d -p 8080:80 nginx
```
#####映射到指定地址的指定端口

可以使用 `ip:hostPort:containerPort` 格式指定映射使用一个特定地址，比如 localhost 地址 127.0.0.1
```
docker run -d -p 127.0.0.1:8080:80 nginx
```

#####映射到指定地址的任意端口
使用 ip::containerPort 绑定 localhost 的任意端口到容器的指定端口，本地主机会自动分配一个端口。
```
docker run -d -p 127.0.0.1::80 nginx
```
还可以使用 udp 标记来指定 udp 端口
```
sudo docker run -d -p 127.0.0.1:8080:80/udp nginx
```

#####查看映射端口配置

使用 docker port 来查看当前映射的端口配置，也可以查看到绑定的地址
```
docker port f6952c68bfd6
443/tcp -> 0.0.0.0:32774
80/tcp -> 0.0.0.0:32775
```

**注：**

* 容器有自己的内部网络和 ip 地址（使用 `docker inspect`可以获取所有的变量，Docker 还可以有一个可变的网络配置。）
* -p 标记可以多次使用来绑定多个端口

例如:
```
docker run -d -p 8080:80  -p 4433:443 nginx
```

###容器互联

>容器的连接(linking)系统是除了端口映射外，另一种跟容器中应用交互的方式。

>该系统会在源和接收容器之间建立一个隧道，接收容器可以看到源容器指定的信息。

#####自定义容器命名

连接系统依据容器的名称来执行。因此，首先需要自定义一个好记的容器命令

创建容器的时候，系统默认会分配一个名字。自定义命令容器有2个好处

* 自定义的命令，比较好记，比如一个web容器可以给它取名web
* 当要连接其他容器的时候，，可以作为一个有用的参考点，比如连接web容器到db容器

