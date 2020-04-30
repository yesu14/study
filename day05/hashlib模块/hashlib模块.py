#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 17:05
# @File: hashlib模块.py
# @Software: PyCharm

import hashlib

m = hashlib.md5()
m.update(b"12345678")
print(m.hexdigest())