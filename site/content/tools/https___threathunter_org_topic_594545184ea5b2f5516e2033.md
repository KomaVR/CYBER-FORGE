---
title: "https://threathunter.org/topic/594545184ea5b2f5516e2033"
description: "
agent节点支持端口复用
agent提供了两种端口复用方法

通过SO_REUSEPORT和SO_REUSEADDR选项进行端口复用
通过iptables进行端口复用(仅支持Linux平台)

通过venom提供的端口复用功能，在windows上可以复用apache、mysql等服务的端口，暂时无法复用RDP、IIS等服务端口，在linux上可以复用多数服务端口。被复用的端口仍可正常对外提供其原有服务。
第一种端口复用方法
# 以windows下apache为例
# 复用apache 80端口，不影响apache提供正常的http服务
# -lhost 的值为本机ip，不能写0.0.0.0，否则无法进行端口复用
./agent.exe -lhost 192.168.204.139 -reuse-port 80

./admin_macos_x64 -rhost 192.168.204.139 -rport 80

第二种端口复用方法
# 以linux下apache为例
# 需要root权限
sudo ./agent_linux_x64 -lport 8080 -reuse-port 80

这种端口复用方法会在本机设置iptables规则，将reuse-port的流量转发到lport，再由agent分发流量
需要注意一点，如果通过sigterm，sigint信号结束程序(kill或ctrl-c)，程序可以自动清理iptables规则。如果agent被kill -9杀掉则无法自动清理iptables规则，需要手动清理，因为agent程序无法处理sigkill信号。
为了避免iptables规则不能自动被清理导致渗透测试者无法访问80端口服务，所以第二种端口复用方法采用了iptables -m recent通过特殊的tcp包控制iptables转发规则是否开启。
这里的实现参考了 
# 启动agent在linux主机上设置的iptables规则
# 如果rhost在内网，可以使用socks5代理脚本流量，socks5代理的使用见下文
python scripts/port_reuse.py --start --rhost 192.168.204.135 --rport 80

# 连接agent节点
./admin_macos_x64 -rhost 192.168.204.135 -rport 80

# 如果要关闭转发规则
python scripts/port_reuse.py --stop --rhost 192.168.204.135 --rport 80

"
external_url: "https://threathunter.org/topic/594545184ea5b2f5516e2033"
category: "Web Exploitation"
---
