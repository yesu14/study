#  @Author  :RG
#  @Time    :2020-04-08 下午 23:56
#  @Note    :用户登录
flag = True # True时继续登录
while flag:
    username = input("Enter your username:")
    password = input("Enter your password:")

    account_locked = 0 #账号未被锁定
    account_not_exit = 0 #账号不存在
    # with open("user.txt","r") as f: #打开文件
    #     data = f.read()
    #     print("读取的用户表数据为:",data)

    lock_file = open("locklist.txt","r+",encoding="utf-8")
    print("------------------------第一步判断账号是否已锁定 start-----------------------------------")
    for lock_line in lock_file.readlines():
        # print("第一步读取lock file",lock_line)
        _line = lock_line.strip("\n").split(",")
        if username == _line[0] and int(_line[1]) > 2:
            print("账号",username,"已被锁定")
            account_locked = 1
    print("------------------------第一步判断账号是否已锁定 end-----------------------------------")
    lock_file.close()

    print("------------------------第二步 判断用户名账号是否正确 start-----------------------------------")
    if account_locked == 0:
        user_file = open("user.txt", "r", encoding="utf-8")
        for user_line in user_file.readlines():
            _line = user_line.strip("\n").split(",")

            _username = _line[0]
            _password = _line[1]
            # print("读取到的行数据：", user_line.strip())
            # print("用户名:",_username)
            # print("密码:",_password)

            if username == _username:
                account_not_exit = 1
                if password == _password:
                    print("欢迎您登录：",username)
                    flag = False
                    break
                else:
                    print("账号或密码不匹配")
                    count = 1  # 密码输错次数,默认为1
                    lock_file = open("locklist.txt", "r+", encoding="utf-8")
                    new_file_data = ""
                    for lock_line in lock_file.readlines():
                        # print("读取lock file", lock_line)
                        line_data = lock_line.strip("\n").split(",")
                        # print("line_data",line_data)
                        if username == line_data[0]:
                            count = int(line_data[1])+1
                            lock_line = lock_line.replace(lock_line,username+","+str(count))
                        new_file_data += lock_line
                    with open("locklist.txt", "w", encoding="utf-8") as f:
                        if count == 1:
                            print("第一次输错,用户名：",username)
                            new_file_data += "\n"+username+","+str(count)
                        f.write(new_file_data)
                        break
                        # else:
                        #     print("累计输错次数count:", count)
                        #     f.write(new_file_data)
                        #     break
        if account_not_exit == 0:
            print("您输入的账号不存在！")


            '''
                1.用户名密码相同
                2.用户名密码不匹配
                3.用户名不存
            '''