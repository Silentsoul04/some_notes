>Nagios是一款开源的网络及服务的监控工具，其功能强大,灵活性强。能有效监控Windows，Linux,Unix等系统的主机各种状态信息，交换机，路由器等网络设备，主机端口及URL服务等。

* 官方网站:[www.nagios.org](https://www.nagios.org/)
* 快速安装说明:[快速安装说明](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/quickstart-fedora.html)

#####Nagios特点:

* 监控网络服务(SMTP,POOP3,HTTP,TCP,PING等)
* 监控主机资源(CPU,负载,IO状态,虚拟及正式内存及磁盘利用率等)
* 简单地插件设计模式使得用户可以方便定制符合自己的服务的监测方法
* 并行服务检查机制
* 具备定义网络分层结构的能力,用"parent"主机定义来表达网络主机间的关系,这种关系可被用于发现和明晰主机宕机或不可达状态
* 当服务或主机问题产生与解决后将报警发送给联系人(mail/im/sound语音)
* 具备定义事件句柄功能，它可以在主机或服务的时间发生时获取更多问题定位
* 自动的日志回滚
* 可以支持并实现对主机的冗余监控(支持分布式监控)
* 可选的WEB界面用于查看当前的网络状态,通知和故障历史，日志文件等

Nagios监控系统家族成员的构成