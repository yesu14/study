#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-24 下午 15:05
#  @Note    :

import time,datetime

def timmer(func):
    def warpper(*args,**kwargs):
        start = time.time()
        func()
        stop = time.time()
        print("运行方法所需时间%s"%(stop-start))
    return warpper
@timmer
def logger():
    for i in range(10):
        time.sleep(0.5)
        print("现在时间：",datetime.datetime.now())

logger()