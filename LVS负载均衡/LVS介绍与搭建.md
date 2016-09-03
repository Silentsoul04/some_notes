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