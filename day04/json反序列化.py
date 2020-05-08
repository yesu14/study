#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-26 下午 15:16
#  @Note    :

import json
import pickle

def test(lalal):
    i = lalal + "来来来"
    print("hahahah",i)

with open("json.txt","rb") as f:
    # data = json.loads(f.read())
    # data = pickle.loads(f.read())
    data = pickle.load(f)
    print(data["name"])
    print(data["方法"]("解决"))

