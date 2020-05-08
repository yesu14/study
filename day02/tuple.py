#  @Author  :RG
#  @Time    :2020-04-13 下午 14:24
#  @Note    :
# print('This is a \033[7;31m test \033[0m!')
# print('This is a \033[1;31;40m test \033[0m!')
# print('\033[1;33;44mThis is a test !\033[0m')
num = input("输入：")
if num.isdigit():
    print(num+"是数字")
else:
    print(num+"不是数字")