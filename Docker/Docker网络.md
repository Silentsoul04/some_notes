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

* 自定义的名字，比较好记，比如一个web容器可以给它取名web
* 当要连接其他容器的时候，，可以作为一个有用的参考点，比如连接web容器到db容器

使用`--name`可以为容器自定义命令
```
docker run -d -P --name web nginx
7440c5acd19bbe1f39c3ab995eec1c628e96f90453e643601c87e15942b36a2a
```
使用`docker ps -l`可以查看命名
```
docker ps -l
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                           NAMES
7440c5acd19b        nginx               "nginx -g 'daemon off"   50 seconds ago      Up 47 seconds       0.0.0.0:32771->80/tcp, 0.0.0.0:32770->443/tcp   web

```

也可以使用`docker inspect`+容器名查看
```
sudo docker inspect -f "{{ .Name }}" 7440c5acd19b
/web
```

注意：容器的名称是唯一的。如果已经命名了一个叫 `web` 的容器，当你要再次使用 `web` 这个名称的时候，需要先用`docker rm` 来删除之前创建的同名容器。

在执行 `docker run` 的时候如果添加 `--rm` 标记，则容器在终止后会立刻删除。注意，`--rm` 和 `-d` 参数不能同时使用。

#####容器互联

使用 `--link` 参数可以让容器之间安全的进行交互。

先创建一个mysql数据库容器
```
docker run --name db -e MYSQL_ROOT_PASSWORD=password -d mysql
ca4ea72397d233520134f3662c79fc4e526403ac65dfc824e1bd41e6d5401042
```

然后创建一个 wordpress 容器，并将它连接到 db 容器
```
docker run --name some-wordpress --link db:mysql -d wordpress
96e27419d4ee53046c0c07ea7915ce1e6fecc9c1f951c74058b78635725f3937
```

wordpress容器建立互联关系。

`--link`参数的格式为 `--link name:alias` name是要连接的容器名字，alias为这个连接的别名
```
docker ps
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                                      NAMES
96e27419d4ee        wordpress             "/entrypoint.sh apach"   2 minutes ago       Up 2 minutes        80/tcp                                     some-wordpress
ca4ea72397d2        mysql                 "docker-entrypoint.sh"   5 minutes ago       Up 5 minutes        3306/tcp                                   db

```

Docker 在两个互联的容器之间创建了一个安全隧道，而且不用映射它们的端口到宿主主机上。在启动 db 容器的时候并没有使用 `-p` 和 `-P` 标记，从而避免了暴露数据库端口到外部网络上。

Docker 通过 2 种方式为容器公开连接信息：

* 环境变量
* 更新 `/etc/hosts` 文件

使用`env`可以查看容器的环境变量:
```
sudo docker run --rm --name wp2 --link db1:db1 wordpress env
HOSTNAME=5a3c2b620bbf
DB1_PORT_3306_TCP_PORT=3306
PHP_INI_DIR=/usr/local/etc/php
PHP_FILENAME=php-5.6.25.tar.xz
DB1_ENV_MYSQL_VERSION=5.7.15-1debian8
DB1_PORT_3306_TCP=tcp://172.17.0.3:3306
DB1_ENV_MYSQL_MAJOR=5.7
DB1_ENV_GOSU_VERSION=1.7
PHPIZE_DEPS=autoconf        file        g++         gcc         libc-dev        make        pkg-config      re2c
WORDPRESS_VERSION=4.6.1
APACHE_ENVVARS=/etc/apache2/envvars
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
GPG_KEYS=0BD78B5F97500D450838F95DFE857D9A90D90EC1 6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3
PWD=/var/www/html
DB1_PORT_3306_TCP_ADDR=172.17.0.3
DB1_PORT_3306_TCP_PROTO=tcp
SHLVL=0
HOME=/root
PHP_SHA256=7535cd6e20040ccec4594cc386c6f15c3f2c88f24163294a31068cf7dfe7f644
WORDPRESS_SHA1=027e065d30a64720624a7404a1820e6c6fff1202
APACHE_CONFDIR=/etc/apache2
DB1_ENV_MYSQL_ROOT_PASSWORD=password
PHP_EXTRA_BUILD_DEPS=apache2-dev
DB1_PORT=tcp://172.17.0.3:3306
DB1_NAME=/wp2/db1
PHP_VERSION=5.6.25
PHP_EXTRA_CONFIGURE_ARGS=--with-apxs2
```

其中 DB1_ 开头的环境变量是供 web 容器连接 db 容器使用，前缀采用大写的连接别名。

除了环境变量，Docker 还添加 host 信息到父容器的 /etc/hosts 的文件。

用户可以链接多个父容器到子容器，比如可以链接多个 web 到 db 容器上。