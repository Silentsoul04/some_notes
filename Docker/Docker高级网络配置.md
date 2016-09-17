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


