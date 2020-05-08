#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-25 下午 23:18
#  @Note    :
# print(all([-1,1]))
# print(bool(-7))
# a = bytes("abcd哈哈哈",encoding="utf-8")
# print(a.decode("utf-8"))

# b = bytearray("abcde",encoding="utf-8")
# print(b[1])
#
# b[1] =20
# print(b)
#
#
# b = bytearray("哈哈哈哈哈",encoding="utf-8")
# b[1] = "哈"
# print(b.decode("utf-8"))

res = filter(lambda n:n>5,range(10))

for i in res:
    print(i)

res1 = map(lambda n:n>5,range(10))

for i in res1:
    print(i)

print("--------------")

res3 = [lambda i:i*2 for i in range(10)]

import functools
res4 = functools.reduce(lambda x,y:x+y,range(10))
print(res4)

print(globals())

print(hash(123))
print(hash(456))
print(hash("哈哈哈"))
print(hash("哈哈哈4"))
print(hash("哈哈哈123"))

def test():
    local_var = "本地！！！！"
    print(locals())
test()
print(globals())
print(locals())