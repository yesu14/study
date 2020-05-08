#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 下午 22:57
#  @Note    :

import socket

client = socket.socket()

client.connect(("localhost",6969))
client.send(b"hello world!")

data = client.recv(1024)

print("发送的数据:".center(50,"-"),data)
client.close()