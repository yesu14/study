#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-08 下午 16:08
#  @Note    :

d1 = {"user01":"1234","user02":"345"}
i = [1,2,3]
try:
    print(d1["user01"])
    # print(i[5])
    # open("text.txt")
except Exception as e:
    print("出错了！！！！",e)
else:
    print("一切正常！")
finally:
    print("我都能执行")
# except KeyError as e:
#     print("出错了！",e)
# except IndexError as e:
#     print("数组出错了",e)