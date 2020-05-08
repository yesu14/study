#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-26 下午 14:38
#  @Note    :

a = {2:4,3:7,6:9,4:2,7:5}
print(sorted(a))
print(sorted(a.items()))
print(sorted(a.values()))
print(sorted(a.items(),key=lambda x:x[1]))
print(sorted(a.items(),key=lambda x:x[0]))

a = [1,2,3,4,5,6]
b =["a","b","c","d"]

f = zip(a,b)
for i in zip(a,b):
    print(i)

print(i for i in zip(a,b))