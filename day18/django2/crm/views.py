from django.http import HttpResponse
from django.shortcuts import render, redirect
import os


# Create your views here.


def home(request):
    print("处理业务。。。")

    # return HttpResponse('<h1>Hello哈哈哈</h1>')
    return render(request,"crm/home.html")


def login(request):
    print("打开登录页面")
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        if user == 'root' and pwd == '1234':
            return redirect('http://banidu.com')
        error_msg = "用户名密码错误1111"
    return render(request, 'crm/login.html', {'msg': error_msg})


USER_LIST = []
for i in range(20):
    list = {"username": "user" + str(i), "age": 12, "sex": "M", "email": "123456@qq.com"}
    USER_LIST.append(list)


def table(request):
    if request.method == "POST":
        username = request.POST.get("username")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        list = {"username": username, "age": age, "sex": sex, "email": email}
        USER_LIST.append(list)
    return render(request, "crm/table.html", {"user_list": USER_LIST})


def regist(request):
    user_info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        sex = request.POST.get("sex")
        faver = request.POST.getlist("faver")
        city = request.POST.getlist("city")
        user_info = [{"username": username, "password": password, "sex": sex, "faver": faver, "city": city}]
        print("user_info", user_info)

        file_list = request.FILES.getlist("files", None)
        if file_list:
            for file_obj in file_list:
                file_path = os.path.join("upload", file_obj.name)
                file = open(file_path, "wb")
                for line in file_obj:
                    file.write(line)
                    file.flush()
                file.close()

        # file_obj = request.FILES.get("file",None)
        # if file_obj:
        #     file_path = os.path.join("upload",file_obj.name)
        #     file = open(file_path,"wb")
        #     for line in file_obj.chunks():
        #         file.write(line)
        #         file.flush()
        #     file.close()
    return render(request, "crm/regist.html", {"user_info": user_info})


from django.views import View


class Register(View):

    def dispatch(self, request, *args, **kwargs):
        print("进入注册页面before...")
        result = super(Register, self).dispatch(request, *args, **kwargs)
        print("after...")
        return result

    def get(self, request):
        print(request.method)
        return render(request, "crm/register.html")

    def post(self, request):
        print(request.method)
        username = request.POST.get("username")
        password = request.POST.get("password")

        return render(request, "crm/register.html")


def get_city(request):
    print("获取城市信息")
    city_dict = {
        "1": "bj",
        "2": "sh",
        "3": "gz",
        "4": "cq",
    }
    return render(request, "crm/city.html", {"city_dict":city_dict})

def detail(request,nid,name):
    print("详情页面",nid,name)
    city_dict = {
        "1": {"name":"北京","renkou":10,"chengqu":"朝阳1,西城1..."},
        "2": {"name":"上海","renkou":50,"chengqu":"朝阳2,西城2..."},
        "3": {"name":"广州","renkou":60,"chengqu":"朝阳3,西城3..."},
        "4": {"name":"重庆","renkou":70,"chengqu":"朝阳4,西城4..."}
    }
    detail = city_dict[nid]
    print(detail)
    return render(request, "crm/detail.html", {"city_dict":detail})