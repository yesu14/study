#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-18 下午 22:36
#  @Note    :
str_choise_buyer = "1"
str_choise_seller = "2"
menu_login = "login" # 返回登录界面
swich_system = True
swich_seller_login = True
swich_seller_item = True
swich_buyer_login = True
swich_buy_item = True
str_login = "Which system do you want to login?\n\033[31m1.Buyer\n2.Seller\n\033[0mYour choise:"
str_buyer = "\033[33mWelcome to the RG Mall!\033[0m"
str_seller = "\033[32mWelcome to the Seller System!\033[0m"
str_welcome = "Welcome\033[7;31m %s \033[0mto the RG Mall".center(50, "*")
str_welcome_seller = "Welcome\033[7;31m %s \033[0mto the Seller System".center(50, "*")
str_wrong_msg = "\033[31mYour input is wrong,please try again later!\033[0m"
str_account_not_exist_msg = "\033[31mAccount does not exist,please try again later!\033[0m"
str_account_wrong_msg = "\033[31mYour account password does not match,please try again later!\033[0m"
str_order_instructions = '''Order instructions:
a.) \033[1;33madd   (syntax: a,item,price;       e.g: a,lg,3000\033[0m)
b.) \033[1;33mmodify(syntax: b,menu,item,price;  e.g: b,2,iphone,2500\033[0m)
c.) \033[1;33mdelete(syntax: c,menu           ;  e.g: c,1\033[0m)
if you want return login menu,please enter \033[31,1mlogin\033[0m
'''
str_balance = "Your balance is \033[31m%s\033[0m"
str_balance_not_enough = "Your balance is\033[31m %s \033[0m,can't buy the product"
str_input_buy_msg = "\033[1;36mPlease enter the product number your want to buy:\033[0m"
str_order_add = "a"  # 添加
str_order_modify = "b"  # 修改
str_order_delete = "c"  # 删除
str_order_complete = "\033[32;1mExecution completed!"

str_order_wrong = "\033[31;1mSyntax input Error,please try again later!"
str_input_order = "please enter your oder:"
str_input_username = "Please enter your username:"
str_input_password = "Please enter your password:"
balance = 0 #余额

#展示商品
def show_item():
    count = 0
    with open("items.txt", "r", encoding="utf-8") as items_file:
        for item in items_file:
            count += 1
            _item = item.strip().split(",")
            print("${num}.${item}:${price}".format(num=count, item=_item[0], price=_item[1]))
        return count

#登录 type=1买家，type=2卖家 file=(买家:user.txt,卖家:seller.txt)
def login(type,username,password,file):
    with open(file,"r",encoding="utf-8") as user_file:
        for line in user_file:
            _line = line.strip().split(",") #解析用户名和密码，文件存储格式为username,password
            if username == _line[0]:
                if password == _line[1]:
                    print(str_welcome % (username))
                    if type == 1:
                        return 1,_line[2]
                    return 1
                else:
                    print(str_account_wrong_msg)
                    return 0
                break
        print(str_account_not_exist_msg)
        return 0

#卖家请求登录时
def seller_login(swich_seller_login,swich_seller_item):
    # 进入卖家系统 可对商品增删改查
    print(str_seller)
    while swich_seller_login:
        username = input(str_input_username)
        password = input(str_input_password)

        if login(2,username,password,"seller.txt") == 1:
            while swich_seller_item:
                show_item()
                print(str_order_instructions)
                order = input(str_input_order)
                order_list = order.split(",")
                # 添加操作
                if order_list[0] == str_order_add and len(order_list) == 3:
                    with open("items.txt", "a+", encoding="utf-8") as items_file:
                        items_file.write("\n" + order_list[1] + "," + order_list[2])
                # 修改操作
                elif order_list[0] == str_order_modify and len(order_list) == 4:
                    with open("items.txt", "w+", encoding="utf-8") as items_file:
                        count = 0
                        for line in items_file:
                            count += 1
                            if str(count + 1) == order_list[1]:
                                _item = line.strip("\n").split(",")
                                line = order_list[2] + "," + order_list[3] + "\n"
                            items_file.write(line)
                            items_file.flush()
                # 删除操作
                elif order_list[0] == str_order_delete and len(order_list) == 2:
                    with open("items.txt", "w+", encoding="utf-8") as items_file:
                        count = 0
                        for line in items_file:
                            count += 1
                            if str(count + 1) == order_list[1]:
                                line += ""
                            items_file.write(line)
                            items_file.flush()
                elif order == menu_login:
                    swich_seller_item = False
                    swich_seller_login = False
                    break
                else:
                    print(str_order_wrong)

#买家登录时
def show_shopping_list(username):
    with open("shopping_list.txt", "r", encoding="utf-8") as shopping_list:
        for line in shopping_list.readlines():
            _line = line.strip("\n").split(",", 1)
            if username == _line[0]:
                print("Your shopping list :")
                list = _line[1].split(",")
                for i, s_list in enumerate(list):
                    print(i, ".", s_list)
                break

#修改用户文件
def modify_user_file(username,balance):
    with open("user.txt","w+",encoding="utf-8") as user_file:
        for line in user_file:
            _line = line.strip("\n").split(",")
            if username == _line[0]:
                line = line[0] + "," + balance + "\n"
            user_file.write(line)
            user_file.flush()
#修改购买列表
def modify_shopping_list(username, item):
    with open("shopping_list.txt", "w+", encoding="utf-8") as shopping_list_file:
        for line in shopping_list_file:
            _line = line.strip("\n").split(",")
            if username == _line[0]:
                # TODO 数组 不能跟字符串直接+  需要处理 shopping_line[1]不能这么写
                items = (line.strip().strip("[").strip("]")).replace(_line[0] + ",", "")
                _list = items.split(",")
                _list.append(item)
                line = _line[0] + "," + str(_list)
            shopping_list_file.write(line)
            shopping_list_file.flush()
#买家请求登录时
def user_login():
    # 进入买家系统 可购买物品
    print(str_buyer)
    swich_buyer_login = True
    while swich_buyer_login:
        username = input(str_input_username)
        password = input(str_input_password)
        result = login(1, username, password, "user.txt")
        if result[0] == 1:
            print(str_balance % (result[1]))
            balance = int(result[1])

            show_shopping_list() #展示购物列表
            print("Product list ".center(50, "*"))
            item_count = show_item() #展示商品列表
            shopping_input = input(str_input_buy_msg)
            if shopping_input.isdigit() and (int(shopping_input) > 0 and int(shopping_input) <= item_count):
                with open("items.txt", "r", encoding="utf-8") as items_file:
                    count = 0
                    for line in items_file:
                        count += 1
                        _line = line.strip("\n").split(",")
                        if count == int(shopping_input):
                            if balance >= int(_line[1]): #余额大于等于商品价格时
                                balance = balance - int(_line[1])  # 设置余额

                                modify_user_file(username,balance)
                                modify_shopping_list(username,_line[0])

                                print("Successful purchase!")
                            else:
                                print(str_balance_not_enough)
            else:
                print(str_wrong_msg)

while swich_system:
    choise_system = input(str_login)
    if choise_system == str_choise_buyer:
        # 进入买家系统 可购买物品
            user_login()
    elif choise_system == str_choise_seller:
        seller_login(True,True)