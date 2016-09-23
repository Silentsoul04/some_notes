top：
功能说明：显示，管理执行中的程序。

语　　法：top [bciqsS][d <间隔秒数>][n <执行次数>]

补充说明：执行top指令可显示目前正在系统中执行的程序，并通过它所提供的互动式界面，用热键加以管理。

参　　数：
　b 　使用批处理模式。 
　c 　列出程序时，显示每个程序的完整指令，包括指令名称，路径和参数等相关信息。 
　d<间隔秒数> 　设置top监控程序执行状况的间隔时间，单位以秒计算。 
　i 　执行top指令时，忽略闲置或是已成为Zombie的程序。 
　n<执行次数> 　设置监控信息的更新次数。 
　q 　持续监控程序执行的状况。 
　s 　使用保密模式，消除互动模式下的潜在危机。 
　S 　使用累计模式，其效果类似ps指令的"-S"参数。


top - 21:13:07 up 2 days, 23:48,  1 user,  load average: 0.00, 0.01, 0.05
Tasks:  84 total,   2 running,  82 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.3 sy,  0.0 ni, 98.0 id,  1.3 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   1017832 total,   740896 used,   276936 free,    75284 buffers
KiB Swap:        0 total,        0 used,        0 free.   417872 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND                                                                                                                    
17308 root      20   0   23540   1540   1116 R  0.3  0.2   0:00.04 top                                                                                                                        
18630 root      20   0    7372   6096    468 S  0.3  0.6   3:08.01 sap1002                                                                                                                    
    1 root      20   0   33568   2656   1260 S  0.0  0.3   0:01.36 init                                                                                                                       
    2 root      20   0       0      0      0 S  0.0  0.0   0:00.00 kthreadd                                                                                                                   
    3 root      20   0       0      0      0 S  0.0  0.0   0:00.94 ksoftirqd/0                                                                                                                
    5 root       0 -20       0      0      0 S  0.0  0.0   0:00.00 kworker/0:0H                                                                                                               
    6 root      20   0       0      0      0 S  0.0  0.0   0:00.00 kworker/u2:0         