#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 14:30
# @File: shutil模块.py01
# @Software: PyCharm

import shutil
import zipfile

# t1 = open("test.txt",encoding="UTF-8")
# t2 = open("test4.txt","w",encoding="UTF-8")

# shutil.copyfileobj(t1,t2)
# shutil.copyfile("test.txt","t3.txt")
# shutil.make_archive("test1","zip","D:\\workspace\\Pycharm\\ttdbb\\study\\day05\\","D:\\workspace\\Pycharm\\ttdbb\\study\\day04\\")

# z = zipfile.ZipFile("t4.zip","w")
# z.write("t3.txt")
# z.write("test.txt")
# z.close()

z = zipfile.ZipFile("t4.zip","r")
z.extractall("day07")
z.close()