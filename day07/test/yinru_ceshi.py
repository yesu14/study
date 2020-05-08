#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 上午 0:26
#  @Note    :

class Test(object):
    def __init__(self):
        print("123")
    def show(self):
        print(456)

from yinru import Test
t = Test()
print(t)