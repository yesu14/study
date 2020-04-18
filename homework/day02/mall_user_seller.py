#  @Author  :RG
#  @Time    :2020-04-14 下午 22:57
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
str_welcome_buyer = "Welcome\033[7;31m %s \033[0mto the RG Mall".center(50, "*")
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
while swich_system:
    choise_system = input(str_login)
    if choise_system == str_choise_buyer:
        # 进入买家系统 可购买物品
        print(str_buyer)
        swich_buyer_login = True
        while swich_buyer_login:
            username = input(str_input_username)
            password = input(str_input_password)
            with open("user.txt","r",encoding="utf-8") as user_file:
                while swich_buy_item:
                    for line in user_file:
                        _line = line.strip("\n").split(",")
                        if username == _line[0]:
                            if password == _line[1]:
                                print(str_welcome_buyer %(username))
                                print(str_balance %(_line[2]))
                                balance = int(_line[2])

                                with open("shopping_list.txt","r",encoding="utf-8") as shopping_list:
                                    for line in shopping_list.readlines():
                                        _line = line.strip("\n").split(",",1)
                                        if username == _line[0]:
                                            print("Your shopping list :")
                                            list = _line[1].split(",")
                                            for i,s_list in enumerate(list):
                                                print(i,".",s_list)
                                            break
                                count_product = 0;
                                print("Product list ".center(50,"*"))
                                with open("items.txt","r",encoding="utf-8") as items_file:
                                    for i,line in enumerate(items_file.readlines()):
                                        _item = line.strip("\n").split(",")
                                        print(i + 1, ".", _item[0], _item[1])
                                        count_product +=1
                                    shopping_input = input(str_input_buy_msg)
                                    if shopping_input.isdigit() and (int(shopping_input)>0 and int(shopping_input)<=count_product):
                                        with open("items.txt", "r", encoding="utf-8") as items_file2:
                                            for i,line in enumerate(items_file2.readlines()):
                                                _item = line.strip("\n").split(",")
                                                if i+1 == int(shopping_input):
                                                   if balance >= int(_item[1]):
                                                       balance = balance-int(_item[1]) #设置余额
                                                       user_file_new = ""
                                                       item_file_new = ""
                                                       for user in user_file.readlines():
                                                           user_file_line = user.strip("\n").split(",")
                                                           if username == user_file_line[0]:
                                                               user_file_new = user_file_line[0]+","+balance+"\n"
                                                               continue
                                                           user_file_new += user
                                                       shopping_file_new = ""
                                                       with open("shopping_list.txt", "r", encoding="utf-8") as shopping_file:
                                                            for shopping in shopping_file.readlines():
                                                                shopping_line = shopping.strip("\n").split(",")
                                                                if username == shopping_line[0]:
                                                                    #TODO 数组 不能跟字符串直接+  需要处理 shopping_line[1]不能这么写
                                                                    s = (shopping.strip("\n").strip("[").strip("]")).replace(shopping_line[0]+",","")
                                                                    print(s)
                                                                    _list = s.split(",")
                                                                    _list.append(_item[0])
                                                                    shopping_file_new += shopping_line[0]+","+str(_list)
                                                                    continue
                                                                shopping_file_new += str(shopping)
                                                        # 修改用户文件里的余额
                                                       with open("user.txt","w",encoding="utf-8") as new_file_user:
                                                            new_file_user.write(user_file_new)
                                                        # 添加购买商品(shopping_list.txt)
                                                       with open("shopping_list.txt","w",encoding="utf-8") as new_file_items:
                                                            new_file_items.write(shopping_file_new)
                                                       print("Successful purchase!")
                                                   else:
                                                       print(str_balance_not_enough)
                                    else:
                                        print(str_wrong_msg)
                            else:
                                print(str_account_wrong_msg)
                                break
                print(str_account_not_exist_msg)
    elif choise_system == str_choise_seller:
        # 进入卖家系统 可对商品增删改查
        print(str_seller)
        swich_seller_login = True
        while swich_seller_login:
            swich_seller_item = True
            username = input(str_input_username)
            password = input(str_input_password)
            with open("seller.txt", "r", encoding="utf-8") as user_file:
                for line in user_file:
                    _line = line.strip("\n").split(",")
                    if username == _line[0]:
                        if password == _line[1]:
                            print(str_welcome_seller % (username))
                            # 操作商品
                            while swich_seller_item:
                                with open("items.txt", "r", encoding="utf-8") as items_file:
                                    for index, item in enumerate(items_file.readlines()):
                                        _item = item.strip("\n").split(",")
                                        print(index + 1, ".", _item[0], _item[1])
                                    print(str_order_instructions)
                                    order = input(str_input_order)
                                    order_list = order.split(",")
                                    item_file_content = ""
                                    # 添加操作
                                    if order_list[0] == str_order_add and len(order_list) == 3:
                                        with open("items.txt", "a+", encoding="utf-8") as temp_file:
                                            temp_file.write("\n" + order_list[1] + "," + order_list[2])
                                    # 修改操作
                                    elif order_list[0] == str_order_modify and len(order_list) == 4:
                                        with open("items.txt", "r", encoding="utf-8") as temp_file:
                                            for index,line in enumerate(temp_file.readlines()):
                                                if str(index+1) == order_list[1]:
                                                    _item = line.strip("\n").split(",")
                                                    item_file_content += order_list[2]+","+order_list[3]+"\n"
                                                    continue
                                                item_file_content += line
                                    # 删除操作
                                    elif order_list[0] == str_order_delete and len(order_list) == 2:
                                        with open("items.txt","r",encoding="utf-8") as temp_file:
                                            for index,line in enumerate(temp_file.readlines()):
                                                if str(index+1) == order_list[1]:
                                                    item_file_content += ""
                                                    continue
                                                item_file_content += line
                                    elif order == menu_login:
                                        swich_seller_item = False
                                        swich_system = False
                                        break
                                    else:
                                        print(str_order_wrong)

                                    if item_file_content != "":
                                        with open("items.txt","w",encoding="utf-8") as items_file_write:
                                            items_file_write.write(item_file_content)
                                            print(str_order_complete)
                print(str_account_wrong_msg)
