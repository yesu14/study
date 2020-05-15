from django.shortcuts import render
# Create your views here.

def home(request):
    print("cms系统")
    return render(request,"cms/home.html")
