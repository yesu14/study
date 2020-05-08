#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 下午 15:12
#  @Note    :

def talk(self):
    print("%s在说话" %self.name)

class User(object):
    def __init__(self,name):
        self.name = name
    def eat(self,name):
        print("%s在吃东西"%name)

user = User("用户1")
choice = input("请输入方法名>>:")
delattr(user,choice)

if hasattr(user,choice):
    func = getattr(user,"choice")
    func("用户2")
else:
    print("进入else")
    setattr(user, "eat", talk)
    talk(user)

    # print(hasattr(user,"eat"))

    func = getattr(user,"eat")
    func(user)


