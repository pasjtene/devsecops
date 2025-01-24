"""
URL configuration for globepy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home_page),
    path('', views.flex_start_home_page),
    path('lms/',include('lms.urls')),
    path('dasboard/',include('dasboard.urls')),
    path('home/', views.home_page),
    path('flexhome/', views.flex_start_home_page, name='homepage'),
    path('blog/', views.blog, name='blogurl'),
    path('blogdetails/', views.blog_details),
    path('admin1235/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/',include("django.contrib.auth.urls")),
    path('hello/', views.say_hello),
    path('hello2/', views.say_hello2, name='hello2'),
    path('hello3/', views.say_hello3),
    path('hello4/', views.say_hello4),
    path('login/',views.login)
    
]
