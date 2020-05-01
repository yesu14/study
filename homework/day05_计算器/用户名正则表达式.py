#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-30 下午 23:26
#  @Note    :

# 除了 [1-0]，[+-*/],[()]
str_wrong_msg = '''
要求：
1.第一个字符不能够为数字
2.长度不能小于7位
3.长度不能超过15位
'''

# a12345678901234567890
import re

print(re.search("ab*","abbbbbbbbbbcccccccabccccc"))

def check_username(username):
    # regExp = "^[\D+{7}]{7,20}$"
    # regExp = "^[a-z0-9A-Z]*{7,20}$"
    regExp = "^[a-zA-Z]{1}[a-zA-Z0-9]{6,14}$"
    # print(re.search(regExp,username))
    if re.search(regExp,username):
        print("输入正确！")
        # return True
    else:
        print("输入有误，请重新输入！\n",str_wrong_msg)
    return False

while True:
    username = input("请输入用户名：")
    if check_username(username):
        break