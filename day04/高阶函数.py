#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/24 15:50
# @File: 高阶函数.py01
# @Software: PyCharm

def test1(name):
    print(name)

def test2(method):
    print("test2!")
    print("运行方法",method)
    method()

# test2(test1)