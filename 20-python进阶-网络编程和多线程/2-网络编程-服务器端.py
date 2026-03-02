"""
服务器端开发流程：
    1.创建服务器端socket对象
    2.绑定IP地址和端口号
    3.设置最大监听书
    4.等待客户端申请建立连接
    5.给客户端发送消息
    6.接收客户端的信息并打印
    7.释放资源
细节：
    客户端和服务端是通过字节流（bytes）的形式实现的
"""
import socket
# 1.创建服务器端socket对象
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.绑定IP地址和端口号
server_socket.bind(('localhost',10086))
# 3.设置最大监听书
server_socket.listen(5)
# 4.等待客户端申请建立连接
accept_socket, client_info = server_socket.accept()
while True:

    msg = input('请输入发送给客户端的消息:')
    if msg == 'exit':
        break
    # 5.给客户端发送消息
    accept_socket.send(msg.encode("utf-8"))
    # accept_socket.send(b'Welcome to socket')
    # 6.接收客户端的信息并打印
    data = accept_socket.recv(1024).decode("utf-8")
    print(f'服务器端收到来自{client_info}的消息是：{data}')
accept_socket.close()

#　扩展；设置端口号重用，目的是：快速重启服务器（服务器关闭后，立即释放端口）
# 参1 当前的套接字对象，参2 选项名，参3 该选项的值
# server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)