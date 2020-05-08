#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 上午 0:30
#  @Note    :
# class Test(object):
#     def __init__(self):
#         print("123")
#     def show(self):
#         print(456)
#
# t = Test()
# print(type(Test))
# print(type(t))

def func(self):
    print("HELLO!",self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type("Foo",(object,),{"talk":func,"__init__":__init__})

f = Foo("user",23)
f.talk()
print(type(Foo))