#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-25 下午 23:08
#  @Note    :

it = iter([1,2,3,4,5,6])
print(next(it))
print(next(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())r
print(next(it))

with open("1.txt","r") as f:
    f.__next__()