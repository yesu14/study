from django.shortcuts import render,redirect


# Create your views here.

def home(request):
    print("cms系统")
    return render(request, "cms/home.html")


from cms import models


def regist(request):
    print("进入注册页面")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # age = request.POST.get("age")
        # 创建数据 1
        # models.UserInfo.objects.create(
        #     username=username,
        #     password=password
        #     # age=age
        # )
        # 创建数据 2
        dic = {"username": username, "password": password}
        models.UserInfo.objects.create(
            **dic
        )
        # 创建数据3
        # obj = models.UserInfo(
        #     username=username,
        #     password=password
        # )
        # obj.save()
        print("数据保存成功")
    # result = models.UserInfo.objects.all()
    # models.UserInfo.objects.filter(id=1).delete()
    # models.UserInfo.objects.update(password="999")
    result = models.UserInfo.objects.filter(id=2).update(password='88')
    print(result)
    return render(request, "cms/regist.html")


def regist2(request):
    msg = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        result = models.UserInfo.objects.filter(username=username)
        if result:
            msg = '用户名已存在！'
            return render(request, "cms/regist2.html", {'msg': msg})
        else:
            models.UserInfo.objects.create(username=username, password=password)
            print('%s注册成功！' % username)
            return render(request, "cms/login.html", {'msg': msg})
    return render(request, "cms/regist2.html", {'msg': msg})


def login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        result = models.UserInfo.objects.filter(username=username, password=password)
        if result:
            # return render(request, "cms/index.html", {'username': username})
            return redirect("/cms/index?username="+username)
        else:
            msg = '账号或密码错误！'
            return render(request, "cms/login.html", {'msg': msg})
    return render(request, "cms/login.html", {'msg': msg})

def index(request):
    print("打开index")
    username = request.GET.get("username")
    username2 = request.POST.get("username")
    print("username1:",username)
    print("username2:",username2)
    return render(request,"cms/index.html",{"username":username})
