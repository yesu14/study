#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 下午 23:03
#  @Note    :

import socket
server = socket.socket()

server.bind(("localhost",6969))
server.listen()
print("等待接收数据...")
conn,addr = server.accept() #conn 服务端生成的客户端连过来实例
print("有数据进来！",conn,addr)
data = conn.recv(1024)
print("服务器接收的数据:".center(50,"-"),data)
conn.send(data.upper())

server.close()