iptables：

    -h 查看帮助 --help
    -V 查看版本 --version
    -n 地址和端口的数字输出
    -L 列表查看规则
        iptables -L -n 查看iptables规则
    -F 删除所有规则，但不会删除默认规则 --flush
    -X 删除用户自定义的链 --delete-chain
    -Z 对链的计数器清零 --zero

    -t 指定表,不加的话默认为filter表 --table eg: -t filter
    -A 添加规则到指定链的最后一条
    -I 添加规则到指定链的第一条 
    -D 删除规则
    -p 指定协议 --proto  (tcp,udp,icmp)
    -j 指定行为 --jump (ACCEPT(接受) DROP(丢弃) REJECT(拒绝))
    -s 指定来源地址 --source
    -d 指定目标地址  --destination
    --dport 指定目的端口 --destination-port
    --sport 指定源端口   --source-port
    --line-numbers 给规则加上序号


禁止规则:

基本的处理行为：ACCEPT(接受) DROP(丢弃) REJECT(拒绝)

示例:
```
iptables -t filter -A INPUT -p tcp --dport 22 -j DROP  禁止22端口
等价于
iptables -A INPUT -p tcp --dport 22 -j DROP   
```
恢复刚才断掉的ssh连接:

* 去机房重启系统或者登陆服务器删除刚刚的禁止规则
```
iptables -t filter -D INPUT -p tcp --dport 22 -j DROP  禁止22端口
```
* 让机房人员冲去服务器或让机房人员拿用户密码登陆进去
* 通过服务器的远程管理卡管理(推荐)
* 先写一个定时任务，没5分钟就停止防火墙
* 测试环境测试号，写成脚本批量执行

添加规则:
```
iptables -t filter -A INPUT -p tcp --dport 80 -j DROP 
或者
iptables -t filter -I INPUT -p tcp --dport 80 -j DROP 
INPUT 后面加数字能指定插入的序号:
iptables -t filter -I INPUT 2 -p tcp --dport 80 -j DROP 
```
删除规则续小结:
```
iptables -F 删除所有规则
iptables -t filter -D INPUT -p tcp --dport 80 -j DROP
或者
iptables -L -n --line-numbers
iptables -t filter -D 序号
/etc/init.d/iptables restart (用iptables命令行配置的命令都是零时生效的)
```

应用(封ip):
```
awk '{print $1}' /var/log/nginx/access.log|sort|uniq -c|sort -rn -k1
   1702 49.223.186.170
    798 101.226.35.225
    660 160.16.101.244
    501 122.9.2.98
    265 107.167.178.116

iptables -t filter -I INPUT  -p tcp -s 49.223.186.170 --dport 80 -j DROP

```



```
iptables --help

Usage: iptables -[ACD] chain rule-specification [options]
       iptables -I chain [rulenum] rule-specification [options]
       iptables -R chain rulenum rule-specification [options]
       iptables -D chain rulenum [options]
       iptables -[LS] [chain [rulenum]] [options]
       iptables -[FZ] [chain] [options]
       iptables -[NX] chain
       iptables -E old-chain-name new-chain-name
       iptables -P chain target [options]
       iptables -h (print this help information)

Commands:
Either long or short options are allowed.
  --append  -A chain        Append to chain
  --check   -C chain        Check for the existence of a rule
  --delete  -D chain        Delete matching rule from chain
  --delete  -D chain rulenum
                Delete rule rulenum (1 = first) from chain
  --insert  -I chain [rulenum]
                Insert in chain as rulenum (default 1=first)
  --replace -R chain rulenum
                Replace rule rulenum (1 = first) in chain
  --list    -L [chain [rulenum]]
                List the rules in a chain or all chains
  --list-rules -S [chain [rulenum]]
                Print the rules in a chain or all chains
  --flush   -F [chain]      Delete all rules in  chain or all chains
  --zero    -Z [chain [rulenum]]
                Zero counters in chain or all chains
  --new     -N chain        Create a new user-defined chain
  --delete-chain
            -X [chain]      Delete a user-defined chain
  --policy  -P chain target
                Change policy on chain to target
  --rename-chain
            -E old-chain new-chain
                Change chain name, (moving any references)
Options:
[!] --proto -p proto    protocol: by number or name, eg. `tcp'
[!] --source    -s address[/mask][...]
                source specification
[!] --destination -d address[/mask][...]
                destination specification
[!] --in-interface -i input name[+]
                network interface name ([+] for wildcard)
 --jump -j target
                target for rule (may load target extension)
  --goto      -g chain
                              jump to chain with no return
  --match   -m match
                extended match (may load extension)
  --numeric -n      numeric output of addresses and ports
[!] --out-interface -o output name[+]
                network interface name ([+] for wildcard)
  --table   -t table    table to manipulate (default: `filter')
  --verbose -v      verbose mode
  --line-numbers        print line numbers when listing
  --exact   -x      expand numbers (display exact values)
[!] --fragment  -f      match second or further fragments only
  --modprobe=<command>      try to insert modules using this command
  --set-counters PKTS BYTES set the counter during insert/append
[!] --version   -V      print package version.
```
