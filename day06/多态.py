#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-05 上午 0:53
#  @Note    :


class Animal(object):
    def __init__(self,age,sex):
        self.age = age
        self.sex = sex
        print("age:%s sex:%s" %(age,sex))

    def animal_talk(obj):
        obj.talk()

class Dog(Animal):
    def talk(self):
        print("狗在叫")
class Cat(Animal):
    def talk(self):
        print("猫在叫")

dog = Dog(2,3)
cat = Cat(1,2)
Animal.animal_talk(dog)
Animal.animal_talk(cat)