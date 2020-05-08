#  @Author  :RG
#  @Time    :2020-04-13 上午 9:17
#  @Note    :

msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="UTF-8"))
print(msg.encode(encoding="UTF-8").decode(encoding="UTF-8"))

print(type(2**64))
import os
dir = os.popen("dir").read()
print(dir)
# if os.path.exists("../day04") == False:
#     print("文件夹day03不存在")
#     os.mkdir("../day04")
#     if os.path.exists("../day04"):
#         print("文件夹day03创建成功！")
# else:
#     print("文件夹03已存在")
