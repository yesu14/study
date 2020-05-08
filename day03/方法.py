#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-18 下午 14:57
#  @Note    :
import time
def func1():
    logger()
    print(123)

def func2(x):
    logger()
    print(x)

def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("a.txt","a+",encoding="utf-8") as f:
        f.write("%s 产生了日志。。\n" %time_current)
        f.flush()


func1()
time.sleep(1)
func2(2)