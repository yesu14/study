#  @Author  :RG
#  @Time    :2020-04-08 上午 0:22
#  @Note    :
import getpass

_username = "tom"
_password = "1234"
username = input("请输入username：")
# password = getpass.getpass("password")
password = input("请输入password：")
print("您输入的用户名为",username,"密码为", password);
if _username == username and _password == password:
    print("欢迎{username}登陆".format(username=username));
else:
    print("用户名密码不匹配！")

