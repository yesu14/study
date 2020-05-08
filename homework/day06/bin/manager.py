#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-06 下午 23:34
#  @Note    :

import sys,os,re

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append((BASE_PATH))

from core import school

ipt_choise = input("1.注册学生\n2.注册老师：")
ipt_s_info = input("请输入姓名，年龄，性别，id，班级：")
s_info = re.split(",",ipt_s_info)
if ipt_choise == "1":
    s = school.Student(s_info[0],s_info[1],s_info[2],s_info[3],s_info[4])
    school.User.reg(s)
elif ipt_choise == "2":
    t = school.Teacher(s_info[0], s_info[1], s_info[2], s_info[3], s_info[4])
    school.User.reg(t)
