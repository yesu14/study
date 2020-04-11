#  @Author  :RG
#  @Time    :2020-04-08 上午 1:11
#  @Note    :

age_of_oldboy = 20
age = int(input("请输入年龄:"))
if age_of_oldboy == age:
    print("猜对了！")
elif age_of_oldboy >age:
    print("猜小了！")
# elif age_of_oldboy <age:
#     print("猜大了！")
else:
    print("猜大了！")
