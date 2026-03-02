"""
网络编程介绍；
概述：
    网络编程也叫网络通信，Socket通信，即：通信双方都独有自己的socket对象
    数据在socket之间通过，数据报包（UDP协议）或者字节流（ TCP协议）的形式进行传输

"""

# import socket
#
# # 创建socket对象
# # 参1： Address Family,地址族，即：IPv4还是IPv6，默认值是AF_INET（ipv4) AF_INET6（ipv6)
# # 参2： Socket Type,套接字类型，TCP还是UDP，默认值是SOCK_STREAM（TCP) SOCK_DGRAM（UDP)
# socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(socket_server)

"""
输出结果是：<socket.socket fd=328, family=2, type=1, proto=0>
2️⃣ fd=328，fd 是 file descriptor（文件描述符）
每个打开的文件、socket 在操作系统里都会有一个整数标识
这个 328 就是操作系统分配给这个 socket 的编号
它对应 内核里的一个 socket 对象
-------------------------------------
值	名称	说明
2	AF_INET	IPv4
10	AF_INET6	IPv6
1	AF_UNIX	Unix 域 socket
-------------------------------------
值	名称	说明
1	SOCK_STREAM	面向连接的 TCP
2	SOCK_DGRAM	无连接的 UDP
3	SOCK_RAW	原始套接字
--------------------------------------
协议号（protocol number）
0 表示使用默认协议
TCP → 自动选择 TCP 协议
UDP → 自动选择 UDP 协议
"""


# Complete PyCharm-friendly example
n = int(input())
if 1 <= n <= 20:
    for i in range(n):
        print(i * i)





