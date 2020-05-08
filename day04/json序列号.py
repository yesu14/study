#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-26 下午 15:02
#  @Note    :

# import 高阶函数 as n
# n.test1("hahahaha")

import json

import pickle

def test(name):
    print("name:",name)

info = {
    "name":"金美燕",
    "age":22,
    "方法":test
}


with open("json.txt","wb") as f:
    # f.write(json.dumps(info))
    # f.write(pickle.dumps(info))
    pickle.dump(info,f)