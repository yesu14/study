#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 15:35
# @File: shelve模块.py
# @Software: PyCharm
import shelve
import datetime

d = shelve.open("shelve_text")
# # print(d.get("username"))

# info = {"age":22,"username":"user01","password":"abcd"}
# name = ["user03","user04","user05"]
# d["name"] = name
# d["info"] = info
# d["time"] = datetime.datetime.now()

print(d.get("name"))
print(d.get("info"))
print(d.get("time"))
d.close()