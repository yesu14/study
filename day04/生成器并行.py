#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-25 下午 16:50
#  @Note    :

import datetime
def eat(name,num):
    print("准备吃包子！")
    while num>0:
        baozi = yield
        num = num-1
        print("[%s][%s]包子被谁[%s]吃了,包子还剩[%s]"%(datetime.datetime.now(),baozi,name,num))
    return "没有包子！"

def fenpei():
    baozi_total = 10
    user01 = eat("user01",baozi_total/2)
    user02 = eat("user02",baozi_total/2)
    print(user01.__next__())
    print(user02.__next__())

    for i in range(baozi_total):
        user01.send("韭菜馅"+str(i))
        user02.send("芹菜馅"+str(i))

fenpei()