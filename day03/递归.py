#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-20 下午 16:40
#  @Note    :
# def calc(n):
#     print(n)
#     return calc(n+1)
# calc(0)
# count = 0
# def calc(n):
#     global count
#     count += 1
#     print("计数：",count,n)
#     if int(n/2) >0:
#         return calc(int(n/2))
#
# calc(2**64)

def plus():
    # z = x+y
    # print("加法",z)
    return 3

def minus(z,y):
    print(type(plus))
    print("减法",(z-y))

a = 1
b = 2

minus(plus,b)