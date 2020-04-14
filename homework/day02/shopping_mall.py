#  @Author  :RG
#  @Time    :2020-04-14 下午 14:03
#  @Note    :测试git

items = [("iphone",5000),("samsung",4000),("huawei",3000),("xiaomi",2000)]
balance = 0
exit_menu = "q"
shopping_list = [] #购物列表
# 您输入的有误，请重新输入
str_wrong = "\033[31mYour input is wrong,please input again!\033[0m"
str_balance_not_enough = "\033[31mYour balance is not enough,Try again later!\033[0m"
str_welcome = "\033[31m Welcome @RG Shopping Mall!\033[0m".center(50,"*")
print(str_welcome)
while True:
    ipt_salary = input("please enter your salary:")
    if ipt_salary.isdigit() and int(ipt_salary)>=0:
        balance = int(ipt_salary)
        break
    else:
        print(str_wrong)

while True:
    for index,item in enumerate(items):
        print(index+1,".",item[0],item[1])
    menu = input("please enter the menu number you want to buy(if your want quit enter\033[7;31m %s \033[0m):" %(exit_menu))
    if menu == exit_menu:
        print("your shopping list is")
        for index,list in enumerate(shopping_list):
            print(index+1,".",list)
        print("\033[7;33mThe program is end!\033[0m")
        exit()
    elif menu.isdigit() and (int(menu)<=len(items) and int(menu)>0):
        _balance = balance - items[int(menu)-1][1]
        if _balance>=0:
            balance = _balance
            shopping_list.append(items[int(menu)-1])
            print("Purchage Success",items[int(menu)-1][0],"!","Your balance is\033[7;31m %s \033[0m" %(balance))
        else:
            print(str_balance_not_enough)
    else:
        print(str_wrong)
