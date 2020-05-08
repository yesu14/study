#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-04 下午 22:18
#  @Note    :
# PYTHON2 经典类深度优先 D-B-A-C 新式类广度优先
# PYTHON3 经典类和新式类 广度优先 D-B-C-A init横向查完，查询父父类


# class People:#经典类
class People(object): #新式类

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    def talk(self):
        print("%s 可以说话！"%self.name)

    def run(self):
        print("%s 可以跑步！" %self.name)

class Relation(object):
    def __init__(self):
        print("self.name%s"%self.name)
    def make_friends(self,obj):
        print("self.name:%s  obj.name:%s obj:%s"%(self.name,obj.name,obj))
        self.friends.append(obj)

class Man(People,Relation):
    def __init__(self,name,age,money):
        # People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.money = money

    def talk(self):
        People.talk(self)
        print("我是Man里的方法：%s" %self.money)



class Woman(People):

    def shopping(self):
        print("我是Woman的方法")

# people = People("人",23)
# people.talk()
man = Man("男人",22,10000)
# man.talk()
woman = Woman("女人",40)
woman.name = "女人02"
man.make_friends(woman)
print(man.friends[0].name)