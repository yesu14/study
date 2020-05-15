"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.urls import include

urlpatterns = [
    path('admin',admin.site.urls),
    path('cms/',include('cms.urls')),
    path('crm/',include('crm.urls')),
]

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('login', views.login),
    path('table', views.table),
    path('regist', views.regist),
    path('city', views.get_city),
    # re_path('detail-(?P<pid>\d+).html', views.detail),
    # re_path('detail-(?P<pid>\d+)-(?P<nid>).html', views.detail),
    re_path('detail-(?P<nid>\d+)-(?P<name>\w+)',views.detail),
    path('register', views.Register.as_view()),
]
'''