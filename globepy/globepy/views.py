from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

register = template.Library()

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

@register.filter(name='is_in_group')
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).count()>0

@login_required
@user_passes_test(lambda user: is_in_group(user, 'grcusers'))
def say_hello2(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world 2"
    return render(request, "hello.html", {"vars": response_data, "name":"Pascal JT2"})

def login(request):
    return render(request, "auth/login.html")

def blog(request):
    return render(request,"blog.html")

def home_page(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return render(request, "home.html", {"vars": response_data, "name":"Pascal JT"})

def flex_start_home_page(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return render(request,"flex_start_home.html", {"vars": response_data})


def say_hello3(request):
    return JsonResponse({"response":"Hello world json"})

def say_hello4(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return JsonResponse(response_data)