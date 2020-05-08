#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-24 下午 22:19
#  @Note    :
import time,datetime

def logging(func):
    def set_time(*args,**kwargs):
        start = time.time()
        a = "tt"
        b = 2
        func(*args,**kwargs)
        stop = time.time()
        print("方法运行所用时间：%s"%(stop-start))
    return set_time

@logging
def test1():
    for i in range(5):
        time.sleep(0.1)
        print("当前时间:",datetime.datetime.now())

@logging
def test2(name,age):
    print("name=",name,age)

test1()
test2()
