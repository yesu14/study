#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-06 下午 23:01
#  @Note    :


import sys,os,re

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append((BASE_PATH))

from core import school

ipt_s_info = input("请输入学生姓名，年龄，性别，学号，班级：")
s_info = re.split(",",ipt_s_info)
print(s_info)
ipt_choise = input("1.交学费\n2.选择课程：")
if ipt_choise == "1":
    s = school.Student(s_info[0],s_info[1],s_info[2],s_info[3],s_info[4])
    s.pay_tuition(4000)
