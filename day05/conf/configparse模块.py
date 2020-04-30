#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 16:28
# @File: configparse模块.py
# @Software: PyCharm
import configparser
config = configparser.ConfigParser()

# config["默认配置"] = {"最大内存":"512M","最小内存":"256M","版本":"V2.0"}
# config["自定义配置"]={"最大内存":"2G","最小内存":"10M"}
# config["默认配置"]["user01"] = "哈哈哈哈"

# with open("app.ini","w",encoding="utf-8") as configfile:
#     config.write(configfile)



config.read("app.ini",encoding="utf-8")
print(config["默认配置"]["最大内存"])