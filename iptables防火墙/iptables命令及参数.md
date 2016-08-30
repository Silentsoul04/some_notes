iptables：

    -h 查看帮助 --help
    -V 查看版本 --version
    -n 地址和端口的数字输出
    -L 列表查看规则
        iptables -L -n 查看iptables规则
    -F 删除所有规则，但不会删除默认规则 --flush
    -X 删除用户自定义的链 --delete-chain
    -Z 对链的计数器清零 --zero

    -t 指定表,不加的话默认为filter表 --table
    -A 添加规则
    -p 指定协议 --proto  eg:-p tcp


禁止规则:

