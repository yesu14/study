#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-27 下午 14:19
#  @Note    :
from flask import Flask, render_template,request,url_for

'''
导入的这两个模块, Flask 是主体类, render_template 是渲染模板.
'''

# 首先创建一个变量 app, 用于初始化 flask 启动核心
app = Flask(__name__)
'''
感兴趣的可以看一下它的源码, 当我们把 __name__ 传进去后, Flask 的实例化行为:
    (flask 源码) app.py01 -> Flask.__init__()
        (flask 源码) helpers.py01 -> _PackageBoundObject.__init__()
可以看到, Flask 会根据你传的 __name__ 定位到程序 (engine.py01) 所在的根路径.
这个根路径的用处和 render_template 有关. 后面会讲.
'''


@app.route('/buy')
def index():
    print("跳转到buy")
    page = "buyer_login.html"
    return render_template(page)

@app.route('/login_page')
def login_page():
    if type == "1":
        pass
    page = "bank_login.html"
    return render_template(page)

@app.route('/login',methods=["GET","POST"])
def login():
    # 将本函数绑定到路由根地址, 这样我们访问主地址时, 就能看到这个页面
    print("进入了登录方法")
    page = 'buyer_login.html'  # 还未创建, 接下来会写
    result = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        result = "true"
    elif request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
        print(username,password)
        result = "true"
    return result


if __name__ == "__main__":
    # 启动, 启动后访问 http://127.0.0.1:5858 查看
    app.run(host='127.0.0.1', port=5858,debug=True)
    print("启动服务器成功！")