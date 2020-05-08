#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-04 下午 22:39
#  @Note    :
class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class man(people):
    def __init__(self,name,age,money):
        # people.__init__(self,name,age)
        super(man,self).__init__(name,age)
        self.money = money

    def money1(self):
        print("money:%s"%self.money)

m1 = man("user01",23,"1000")
m1.money1()