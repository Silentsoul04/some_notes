####LVS简介      
LVS是`Linux VIrtual Server`的缩写。在98年5月由章文嵩博士组织成立,是国内最早出现的开源软件之一。   

官网:
[www.linuxvirtualserver.org](http://www.linuxvirtualserver.org/zh/)       
      
LVS负载均衡调度技术是在Linux内核中实现的。使用该软件配置LVS时，不能直接配置内核中的ipvs，而需要使用ipvs的管理工具ipvsadm进行管理。也可用keeplived软件直接管理ipvs      
      
LVS:

* 实现调度工具IPVS      
* 管理工具ipvsadm     
* keeplived 实现管理及高可用      

#####LVS术语        
      
* 虚拟ip地址(virtual ip address)      
    * 用于向客户端计算机提供服务的ip地址缩写:vip        
* 真实ip地址(real server ip address)      
    * 在集群下面节点使用的ip地址:缩写rip        
* director的ip地址(director ip address):         
    * director用于连接内外网第ip地址,物理网卡上的ip地址，是负载均衡器的ip 缩写dip     
* 客户端ip地址(client ip address)      
    * 客户端用户计算机请求集群服务器的ip地址,该地址用作发送给集群的请求的源ip地址 缩写cip      
      
#####LVS模式        
      
* NAT模式 ==> 网络地址转换(Network Address Translation)       
* TUN模式 ==> 隧道模式(Tunneling)       
* DR模式  ==> 直接路由模式 (Direct Routing)       
      
#####DR模式（熟练）

* 1.通过在调度器LB上修改数据包的`目的MAC地址`实现转发。注意,源IP地址仍然是CIP,目的IP地址仍然是VIP.
* 2.请求的报文经过调度器,而RS相应处理后的报文无需经过调度器LB,因此并发访问量大时使用效率很高(和NAT模式相比)
* 3.因DR模式是通过MAC地址的改写机制实现的转发，因此所有RS节点和调度器LB只能在一个局域网LAN中(小缺点)
* 4.需要注意RS节点的VIP的绑定(lo:vip,lol:vip)和ARP抑制的问题
* 5.强调下:RS节点的默认网关不需要是调度器LB和DIP,而直接是IDC机房分配的上级路由器的IP(这是RS带油外网IP地址的情况)，理论讲:只要RS可以出网即可，不是必须要配置外网IP
* 6.由于DR模式的调度器仅进行了目的MAC地址的改写，因此，调度器LB无法改变请求的报文和目的端口(和NAT要区别)
* 7.当前，调度器LB支持几乎所有的UNIX,LINUX系统，但目前不支持WINDOWS系统，真实服务器RS节点可以是WINDOWS系统
* 总的来说DR模式效率很高，但是配置也比较麻烦，因此，访问不是特别大的网站可以使用haproxy,nginx代替。这符合简单、易用、高效的原则。
* 直接对外的访问业务,例如,web服务器做RS节点，RS最好用公网IP地址。如果不直接对外的业务，如MySQL存储系统RS节点，最好只用内部IP地址

#####NAT模式
#####TUN模式
#####FULL NAT模式

#####LVS调度算法:

>LVS调度算法决定了如何在集群节点之间分布工作负荷

* 固定调度算法:
    - **rr: 轮询调度(Round-Robin)**
        + 将请求依次分配不同的RS节点,也就是均摊请求。只适合于RS节点处理性能相差不大的情况
    - **wrr:加权轮询调度(Weighted Round-Robin)**
        + 根据不同RS节点的权值分配任务。权值较高的RS将优先获得任务。并且分配到的连接数将比权值较低的RS节点更多。相同权值的RS将得到相同数目的连接数。
    - dh:目的地址哈希调度(Destination Hashing)
    - sh:源地址哈希调度(Source Hashing)
* 动态调度算法(SQD,NQ官方站点没提到,编译LVS可以看到)
    - **wlc:加权最少连接数调度(Weighted Least-Connection)**
        + 假设各台RS的权值一次为Wi(i=1..n),当前TCP连接数依次为Ti(i=1..n)，依次选取Ti/Wi为最小的RS作为下一个分配的Rs
    - lc:最少连接数调度(Least-Connection)
    - lblc:基于地址的最少连接数调度(Locality-Based Least-Connection)
    - lblcr:基于地址带重复最少连接数调度(Locality-Based Least-Connection with Replication)
    - SED: 最短的期望的延迟:(Shortest Expected Delay Scheduling SED)
    - NQ:最少队列调度(Never Queue Scheduling)

####安装LVS软件:

准备:

* 三台服务器或者VM虚拟机
* 数据库及memcache等对内业务的负载均衡环境
    - 10.0.0.4  LVS调度器  对外提供服务的VIP为10.0.0.11
    - 10.0.0.5  RS1(真实服务器)
    - 10.0.0.6  RS2(真实服务器)
    - 上面的环境为内部环境的负载均衡模式，即LVS服务是对内部服务的，如数据库及memcache等的负载均衡
* web服务或webcache等负载均衡环境
    - 192.168.1.17  LVS调度器  对外提供服务的VIP为10.0.0.11
    - 192.168.1.18  RS1(真实服务器)
    - 192.168.1.19  RS2(真实服务器)
    - 假设10.0.0.0/24为内网卡，192.168.1.0/24为外网卡


#####安装LVS


```
ln  -s /usr/src/kernels/2.6.32-642.4.2.el6.x86_64/ /usr/src/linux
wget http://linuxvirtualserver.org/software/kernel-2.6/ipvsadm-1.26.tar.gz
tar zxf ipvsadm-1.26.tar.gz 
cd ipvsadm-1.26

yum install libnl* popt* -y      ###是个坑,没有会报错

make && make install

/sbin/ipvsadm == modprobe ip_vs
lsmod|grep ip_lv
```

#####手动配置LVS

配置vip:

```
ifconfig eth1:0 10.0.0.10/24 up
route add -host 10.0.0.10 dev eth1
```

* ipvsadm 常用选项
    * -C   清空所有
    * -A   添加虚拟服务
    * -t   指定一个vip地址和端口
    * -s   指定调度算法(rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq)
    * -p + 秒数  会话保持时间  
    * -g   DR模式
    * -i   TUN模式
    * -m   NAT模式
    * -w   权重
    * -D   删除虚拟服务
    * -d   删除节点
    * -S   保存
    * -L   列出ipvsadm列表
    * -n   以数字形式显示地址和端口


