#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-20 下午 22:27
#  @Note    :

#最大64/32位系统支持多少G内存

# 1byte -> 1024kb -> 1024mb -> 1024gb

def sys32():
    y = 2**32
    z = y/(1024**3)
    print("32位操作系统最高支持：",z,"GB")

def sys64():
    y = 2**64
    z = y/(1024**3)
    print("64位操作系统最高支持：", z,"GB")
    z1 = y / (1024 ** 4)
    print("64位操作系统最高支持：", z1, "TB")
    z2 = y / (1024 ** 5)
    print("64位操作系统最高支持：", z2, "PB")

sys32()
sys64()