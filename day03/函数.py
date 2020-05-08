#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-20 下午 14:48
#  @Note    :

#默认参数，不传递值用默认参数，有实参用实参
def test(x,y=2):
    print(x)
    print(y)

test(1)

def test(*x):
    print(x)

test(1,2,3,4,5)
test(*(1,2,3,4,5,6,7,8))

def test1(x,*args):
    print(args)

test1(1,2,3,4,5,6,7)

def test2(**kwargs):
    print(kwargs["name"])
    print(kwargs)

test2(name="tom01",age=8)
test2(**{'name':'tom01','age':9})

def test3(name,age=18,**kwargs):
    print(name)
    print(kwargs)

test3("tom",age=9,sex="M")
test3('tommmm',sex="F",age=3,haha="haha")

print("a","b","c",sep="-")

def test5(name,age=5,*args,**kwargs):
    print("name",name)
    print("age",age)
    print(args)
    print(kwargs)

test5("tom0000",3,5,6,7,8,sex="F",s="j")