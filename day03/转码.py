#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-18 上午 11:01
#  @Note    :
import sys
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

s = u"你好"
s_to_gbk = s.encode("utf-8")
# s_to_unicode = s.decode("utf-8")

print(s,type(s))
print(s_to_gbk,type(s_to_gbk))
print(s_to_gbk.decode(),type(s_to_gbk))
# print(s_to_unicode,type(s_to_unicode))