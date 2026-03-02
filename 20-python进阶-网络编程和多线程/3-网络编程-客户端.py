"""
客户端开发流程：
    1.创建客户端socket对象
    2.连接服务器端，指定：服务器端IP,端口号
    3.接收服务器的信息并打印
    4.给服务器发送消息
    5.释放资源
"""
import socket

# 1.创建客户端socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.连接服务器端，指定：服务器端IP,端口号
client_socket.connect(("localhost", 10086))
while True:
    # 3.接收服务器的信息并打印
    data = client_socket.recv(1024).decode("utf-8")
    print("服务器发来的消息是：", data)
    msg = input("请输入要给服务器发送的消息：")
    # 4.给服务器发送消息
    client_socket.send(msg.encode("utf-8"))
# 5.释放资源
client_socket.close()
