#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-25 下午 15:31
#  @Note    :

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        print("变更之后：",n,a,b)
        n+=1
    return "done1"

f = fib(10)

while True:
    try:
        x = next(f)
        print("x:",x)
    except StopIteration as e:
        print("出错了:",e.value)
        # break


# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())