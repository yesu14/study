#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-24 下午 23:01
#  @Note    :

user,pwd = "user01","user01"

def auth(auth_type):
    print(auth_type)
    def login(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("用户名：").strip()
                password = input("密码：").strip()

                if user == username and pwd == password:
                    print("\033[32;1m登录成功，正在跳转中。。。\033[0m")
                    result = func(*args,**kwargs)
                    print("登陆成功1231231231")
                    return result
                else:
                    print("\033[31;1mInvalid account!!!\033[0m")
            else:
                print("LDAP访问服务器！")
        return wrapper
    return login

@auth(auth_type="local")
def index():
    print("index页面")
    return "IIIIIIIIIIIIIINDEX"
@auth(auth_type="ldap")
def home():
    print("home页面")

print(index())
home()

