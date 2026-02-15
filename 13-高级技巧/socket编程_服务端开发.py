# # 创建socket对象
# import socket
# socket_server = socket.socket()
#
# # 绑定socket_server到指定IP和地址
# socket_server.bind("localhost",8888)
# # 服务端开始监听端口
# socket_server.listen(1)
# # back log为int整数，表示允许的连接数量，超出的会等待，可以不填，不填会自动设置一个合理值
#
# # 接收客户端连接，获得连接对象
# conn,address = socket_server.accept()
# print(f"接收到客户端连接，连接来自：{address}")
# # accept方法是阻塞方法，如果没有连接，会卡在当前这一行不会向下执行代码
# # accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素
#
# # 客户端连接后，通过recv方法，接收客户端发送的消息
# while True:
#     data = conn.recv(1024).decode("utf-8")
#     #　recv方法的返回值是字节数组（bytes），可以通过decode使用utf-8解码为字符串
#     # recv方法的传参是buffsize，缓冲区大小，一般设置为1024即可
#     if data =='exit':
#         break
#     print("接收到发送的数据：",data)
#     # 可以通过while true无限循环来持续和客户端进行数据交互
#     # 可以通过判定客户端发来的特殊标记，如exit，来退出无限循环
#
#     # 通过conn(客户端当次连接对象)，调用send方法可以回复消息
#     conn.send("hello".encode("utf-8"))
# # conn(客户端当次连接对象)和socket_server对象调用close方法，关闭连接

"""
演示Socket服务端开发
"""
# import socket
# # 创建Socket对象
# socket_server = socket.socket()
#
# # 绑定ip地址和端口
# socket_server.bind(("localhost", 8888))
# # 监听端口
# socket_server.listen(1)
# # listen方法内接受一个整数传参数，表示接受的链接数量
# # 等待客户端链接
# # result: tuple = socket_server.accept()
# # conn = result[0]        # 客户端和服务端的链接对象
# # address = result[1]     # 客户端的地址信息
# conn, address = socket_server.accept()
# # accept方法返回的是二元元组(链接对象， 客户端地址信息)
# # 可以通过 变量1, 变量2 = socket_server.accept()的形式，直接接受二元元组内的两个元素
# # accept()方法，是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这一行不向下执行了
#
# print(f"接收到了客户端的链接，客户端的信息是：{address}")
#
# while True:
#     # 接受客户端信息，要使用客户端和服务端的本次链接对象，而非socket_server对象
#     data: str = conn.recv(1024).decode("UTF-8")
#     # recv接受的参数是缓冲区大小，一般给1024即可
#     # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
#     print(f"客户端发来的消息是：{data}")
#     # 发送回复消息
#     msg = input("请输入你要和客户端回复的消息：")
#     if msg == 'exit':
#         break
#     conn.send(msg.encode("UTF-8"))
# # 关闭链接
# conn.close()
# socket_server.close()
#

import socket
socket_server = socket.socket()
socket_server.bind(("localhost",8888))
socket_server.listen(1)
conn,address = socket_server.accept()
print(f"接收到了客户端的链接，客户端的信息是：{address}")

while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是：{data}")
    msg = input("请输入你要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))
conn.close()
socket_server.close()

