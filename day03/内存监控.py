#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-23 上午 0:21
#  @Note    :

import sys

def show_memory(unit='KB', threshold=1):
    '''查看变量占用内存情况

    :param unit: 显示的单位，可为`B`,`KB`,`MB`,`GB`
    :param threshold: 仅显示内存数值大于等于threshold的变量
    '''
    from sys import getsizeof
    scale = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}[unit]
    for i in list(globals().keys()):
        memory = eval("getsizeof({})".format(i)) // scale
        if memory >= threshold:
            print(i, memory)


if __name__ == '__main__':
    a = [i for i in range(10000)]
    print(a)
    show_memory()
    # a 85

# s = 1
# s1 = "a"
# s2 = "哈"
# print(s.__sizeof__(),s)
# print(s1.__sizeof__(),s1)
# print(s2.__sizeof__(),s2)
# print(sys.getsizeof(s))
# print(sys.getsizeof(s1))
# print(sys.getsizeof(s2))

# for i in range(10000):
#     d = str(i)
#     s = d
#     print(d.__sizeof__(),d)
#     print("s=",s.__sizeof__(),s)

