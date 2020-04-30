#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 22:14
# @File: 正则表达式.py
# @Software: PyCharm

import re
import time
# s = "abcdefg#123#hahasd3"
# sign = "#.+#"
# start = time.time()
# print(re.search(sign,s))
# end = time.time()
# print("运行时间=",(end-start))

s1 = "abcaac"
t1 = "aa?"

print(re.search(t1,s1))