高级网络配置
=====================

当 Docker 启动时，会自动在主机创建一个 `docker0` 虚拟网桥，实际上是Linux的一个`bridge` 可以理解为一个软件交换机。它会在挂载到他的网卡之间进行转发。

同时,Docker 随机分配一个本地未占用的私有网络中一个地址`docker0`接口。比如典型的`172.17.42.1`,掩码为`255.255.0.0` 。此后启动的容器内的网口也会分配一个同一个 网段的地址。

当创建一个 Docker 容器时，同时会创建一对`veth pair`接口(当数据包发送到一个端口时，另外一个端口也可以接到相同的数据包)。这对接口一端在容器内，即`eth0`，另一端在本地被挂载到`docker0`网桥，名称以`veth`开头(例如veth197ec5a)。通过这种方式,主机可以跟容器通信，容器之间也可以互相通信。Docker就创建了在主机和所有容器之间一个虚拟共享网络。

![Docker网络](_images/Docker网络.png)

接下来的部分将介绍在一些场景中，Docker 所有的网络定制配置。以及通过 Linux 命令来调整、补充、甚至替换 Docker 默认的网络配置。

####快速配置

>下面是一个跟 Docker 网络相关的命令列表:

>其中有些命里只有在Docker服务启动时才能配置，而且不能马上生效

* `-b BRIDGE or --bridge=BRIDGE` 指定容器挂载的网桥
* `--bip=CIDR` 定制 `docker0` 的掩码
* `-H SOCKET or --host=SOCKET...`  Docker服务端接收命令的通道
* `--icc=true|false` 是否支持容器之间进行的通信
* `--ip-forward=true|false` 是否允许Docker容器添加iptables规则
* `--mtu=BYTES` 容器网络中的MTU

下面两个命令既可以在启动服务时指定，也可以在容器启动时(`docker run`)指定。在Docker服务启动的时候指定则会称为默认值，后面`docker run`时可以覆盖设置的默认值

* `--dns=IP_ADDRESS`  使用指定的DNS服务器
* `--dns-search=DOMAIN` 指定DNS搜索域

下面这些选项只有在`docker run `执行的时候用，因为它针对容器的特性内容:

* `-h HOSTNAME or --hostname=HOSTNAME` 配置容器主机名
* `--link=CONTAINER_NAME:ALIAS` 添加到另一个容器的连接
* `--net=bridge|none|container:NAME_or_ID|HOST` 配置容器的桥接模式
* `-p SPEC or -publish=SPEC` 映射容器端口到宿主主机
* `-P or --publish-all=true|false` 映射容器所有端口到宿主主机

#####配置DNS
Docker 没有为每个容器专门定制镜像，那么怎么自定义配置容器的主机名和 DNS 配置呢？ 秘诀就是它利用虚拟文件来挂载到来容器的 3 个相关配置文件。

在容器中使用 mount 命令可以看到挂载信息：

```
$ mount
...
/dev/mapper/centos-root on /etc/resolv.conf type xfs (rw,relatime,attr2,inode64,noquota)
/dev/mapper/centos-root on /etc/hostname type xfs (rw,relatime,attr2,inode64,noquota)
/dev/mapper/centos-root on /etc/hosts type xfs (rw,relatime,attr2,inode64,noquota)
...
```

这种机制可以让宿主主机 DNS 信息发生更新后，所有 Docker 容器的 dns 配置通过 /etc/resolv.conf 文件立刻得到更新。

如果用户想要手动指定容器的配置，可以利用下面的选项:

* `-h HOSTNAME or --hostname=HOSTNAME` 设定容器的主机名，它会被写到容器内的 `/etc/hostname` 和 `/etc/hosts`。但它在容器外部看不到，既不会在 docker ps 中显示，也不会在其他的容器的 /etc/hosts 看到。

* `--link=CONTAINER_NAME:ALIAS` 选项会在创建容器的时候，添加一个其他容器的主机名到`/etc/hosts` 文件中，让新容器的进程可以使用主机名 `ALIAS` 就可以连接它。

* `--dns=IP_ADDRESS` 添加 DNS 服务器到容器的 `/etc/resolv.conf` 中，让容器用这个服务器来解析所有不在 `/etc/hosts` 中的主机名。

* `--dns-search=DOMAIN` 设定容器的搜索域，当设定搜索域为 `.example.com `时，在搜索一个名为 `host` 的主机时，DNS 不仅搜索 host，还会搜索 `host.example.com`。 注意：如果没有上述最后 2 个选项，Docker 会默认用主机上的 `/etc/resolv.conf` 来配置容器。

#####容器访问控制

容器的访问控制，主要通过 Linux 上的 iptables 防火墙来进行管理和实现。iptables 是 Linux 上默认的防火墙软件，在大部分发行版中都自带。

#####容器访问外部网络

容器要想访问外部网络，需要本地系统的转发支持。在Linux 系统中，检查转发是否打开。
```
$sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
```

如果为 0，说明没有开启转发，则需要手动打开。
```
$sysctl -w net.ipv4.ip_forward=1
```
如果在启动 Docker 服务的时候设定 `--ip-forward=true`, Docker 就会自动设定系统的 ip_forward 参数为 1。

####容器之间访问

容器之间相互访问，需要两方面的支持:

* 容器的网络拓扑是否已经互联。默认情况下，所有容器都会被连接到 docker0 网桥上。
* 本地系统的防火墙软件 -- iptables 是否允许通过。

#####访问所有端口

当启动 Docker 服务时,默认会添加一条转发策略到 iptables 的 FORWARD 链上。此策略是 accept 还是 drop 取决于 `--icc=true` 还是`--icc=false`。当然如果手动指定`--iptables=false`是不会添加iptables规则的。

可见，默认情况下，不同容器之间是允许容器网络互通的，如果处于安全考虑，可以在`/etc/default/docker`文件中配置 `DOCKER_OPTS=--icc=false` 来禁止它。

#####访问指定端口

在通过 `-icc=false` 关闭网络访问后，还可以通过 `--link=CONTAINER_NAME:ALIAS` 选项来访问容器的开放端口。

