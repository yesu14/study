#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 下午 16:36
#  @Note    :

class MyException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message

try:
    git_successful = True
    if git_successful:
        pass
    else:
        raise MyException("git出错，稍后请尝试！")
except MyException as e:
    print(e)

def func(type,name,password):
    pass