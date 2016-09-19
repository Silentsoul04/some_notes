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

####端口映射

#####映射容器端口到宿主主机

默认情况下，容器可以主动访问到外部网络的连接，但是外部网络无法访问到容器。

#####容器访问外部
容器所有到外部网络的连接，源地址都会被NAT成本地系统的IP地址。这是使用 iptables 的源地址伪装操作实现的。

查看主机的 NAT 规则。

```
sudo iptables -t nat -nL
...
MASQUERADE  all  --  172.17.0.0/16        0.0.0.0/0           
...
```
其中，上述规则将所有源地址在 172.17.0.0/16 网段，目标地址为其他网段（外部网络）的流量动态伪装为从系统网卡发出。MASQUERADE 跟传统 SNAT 的好处是它能动态从网卡获取地址。

#####外部访问容器

容器允许外部访问，可以在 docker run 时候通过 -p 或 -P 参数来启用。

不管用那种办法，其实也是在本地的 iptable 的 nat 表中添加相应的规则。

使用 -P 时：
```
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:32768 to:172.17.0.4:80
```

使用 -p 80:80 时：
```
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:80 to:172.17.0.2:80
```

注意：

* 这里的规则映射了 `0.0.0.0`，意味着将接受主机来自所有接口的流量。用户可以通过 `-p IP:host_port:container_port` 或 `-p IP::port` 来指定允许访问容器的主机上的 IP、接口等，以制定更严格的规则。
* 如果希望永久绑定到某个固定的 IP 地址，可以在 Docker 配置文件 `/etc/default/docker` 中指定 `DOCKER_OPTS="--ip=IP_ADDRESS，之后重启 Docker 服务即可生效。

#####配置 docker0 网桥

Docker服务会默认创建一个 `docker0` 网桥(其上有一个 `docker0` 内部接口),它在内核层连接其他物理或虚拟网卡，这就将所有容器和本地主机都放在同一个物理网络。

Docker 默认指定了 `docker0` 接口 的 IP 地址和子网掩码，让主机和容器之间可以通过网桥相互通信，它还给出了 MTU（接口允许接收的最大传输单元），通常是 1500 Bytes，或宿主主机网络路由上支持的默认值。这些值都可以在服务启动的时候进行配置。

* --bip=CIDR -- IP 地址加掩码格式，例如 192.168.1.5/24
* --mtu=BYTES -- 覆盖默认的 Docker mtu 配置

也可以在配置文件中配置 DOCKER_OPTS，然后重启服务。 由于目前 Docker 网桥是 Linux 网桥，用户可以使用` brctl show` 来查看网桥和端口连接信息。
```
sudo brctl show
bridge name     bridge id               STP enabled     interfaces
docker0         8000.3a1d7362b4ee       no              veth65f9
                                             vethdda6
```
注：brctl 命令在 Debian、Ubuntu 中可以使用 sudo apt-get install bridge-utils 来安装。

每次创建一个新容器的时候，Docker 从可用的地址段中选择一个空闲的 IP 地址分配给容器的 `eth0` 端口。使用本地主机上 `docker0` 接口的 IP 作为所有容器的默认网关。
```
sudo docker run -i -t --rm ubuntu:12.04 /bin/bash

root@eb7f66531a59:/# ip addr show eth0
10: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:ac:11:00:05 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.5/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:5/64 scope link 
       valid_lft forever preferred_lft forever
root@eb7f66531a59:/# ip route
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0  proto kernel  scope link  src 172.17.0.5 
```

#####自定义网桥

>除了默认的 docker0 网桥，用户也可以指定网桥来连接各个容器。

在启动 Docker 服务的时候，使用 `-b BRIDGE` 或 `--bridge=BRIDGE`来指导使用的网桥。

如果服务已经运行，那需要先停止服务，并删除旧的网桥。
```
$ sudo service docker stop
$ sudo ip link set dev docker0 down
$ sudo brctl delbr docker0
```
然后创建一个网桥 bridge0。
```
$ sudo brctl addbr bridge0
$ sudo ip addr add 192.168.5.1/24 dev bridge0
$ sudo ip link set dev bridge0 up
```
查看确认网桥创建并启动。
```
$ ip addr show bridge0
4: bridge0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state UP group default
    link/ether 66:38:d0:0d:76:18 brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.1/24 scope global bridge0
       valid_lft forever preferred_lft forever
```
配置 Docker 服务，默认桥接到创建的网桥上。
```
$ echo 'DOCKER_OPTS="-b=bridge0"' >> /etc/default/docker
$ sudo service docker start
```
启动 Docker 服务。 新建一个容器，可以看到它已经桥接到了 bridge0 上。

可以继续用 brctl show 命令查看桥接的信息。另外，在容器中可以使用 ip addr 和 ip route 命令来查看 IP 地址配置和路由信息。

#####工具和示例

* pipework
    * Jérôme Petazzoni 编写了一个叫 pipework 的 shell 脚本，可以帮助用户在比较复杂的场景中完成容器的连接。

* playground
    * Brandon Rhodes 创建了一个提供完整的 Docker 容器网络拓扑管理的 Python库，包括路由、NAT 防火墙；以及一些提供 HTTP, SMTP, POP, IMAP, Telnet, SSH, FTP 的服务器。

#####编辑网络配置文件

Docker 1.2.0 后支持在运行中的容器里编辑 /etc/hosts, /etc/hostname 和 /etc/resolve.conf 文件。

但是这些修改是临时的，只在运行的容器中保留，容器终止或重启后并不会被保存下来。也不会被 docker commit 提交。
