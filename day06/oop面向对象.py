#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-04 下午 15:47
#  @Note    :

class user:

    # 构造函数
    def __init__(self,username):
        print(username)
        if(username=="user01"):
            age = 50
        pass

    # 析构函数
    def __del__(self):

        print("class生命周期已经结束")
        pass

    def show(self,name):
        print("show方法：",self)
        print("show方法(username)：",name)


user01 = user()
user01.show("123","f = open()")

# user02 = user("user000002","345",55)
# user02.show()