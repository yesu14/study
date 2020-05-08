#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-25 上午 0:18
#  @Note    :
import time,sys

# a = [i*2 for i in range(100000)]
# print(a)

# b = (i*2 for i in range(100000))
# print(b)

def test1():
    start = time.time()
    a = [i*2 for i in range(10000000)]
    end = time.time()
    # print(a)
    print(type(a))
    print(id(a))
    print(sys.getsizeof(a))
    print(int(sys.getsizeof(a))/(1024*1024))
    print("1所耗时间：%s",end-start)

def test2():
    start = time.time()
    a = (i*2 for i in range(10000000))
    end = time.time()
    # for i in a:
    #     print(i)
    print(type(a))
    print(id(a))
    print(sys.getsizeof(a))
    print("2所耗时间：%s", end - start)

test1()
print("****************")
test2()