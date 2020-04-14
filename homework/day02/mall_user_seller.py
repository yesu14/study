#  @Author  :RG
#  @Time    :2020-04-14 下午 22:57
#  @Note    :
str_choise_buyer = "1"
str_choise_seller = "2"
str_login = "Which system do you want to login?\n\033[31m1.Buyer\n2.Seller\033[0m"
str_buyer = "\033[33mWelcome to the RG Mall!\033[0m"
str_seller = "\033[32mWelcome to the Seller System!\033[0m"
str_welcome_buyer = "Welcome\033[7;31m %s \033[0mto the RG Mall".center(50,"*")
str_welcome_seller = "Welcome\033[7;31m %s \033[0mto the Seller System".center(50,"*")
str_wrong_msg = "\033[31mYour input is wrong,please try later!\033[0m"
str_account_wrong_msg = "\033[31mYour account password does not match!please try later"
str_input_username = "Please enter your username:"
str_input_password = "Please enter your password:"
while True:
    choise_system = input(str_login)
    if choise_system == str_choise_buyer:
        # 进入买家系统 可购买物品
        print(str_buyer)
        username = input(str_input_username)
        password = input(str_input_password)
    elif choise_system == str_choise_seller:
        # 进入卖家系统 可对商品增删改查
        print(str_seller)
        username = input(str_input_username)
        password = input(str_input_password)
        user_file = open("seller.txt", "r", encoding="utf-8")
        for line in user_file:
            if username == list(line)[0]:
                if password == list(line)[1]:
                    print(str_welcome_seller %(username))
                else:
                    print()
                break

    else:
        print(str_wrong_msg)
