from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('LMS --- Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

def say_hello2(request):
    response_data = {}
    response_data["erro"] = "LMS -- No error found"
    response_data["message"] = "Hello world"
    return render(request, "hello.html", {"vars": response_data, "name":"Pascal JT"})

def say_hello3(request):
    return JsonResponse({"response":"Hello world json"})

def say_hello4(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return JsonResponse(response_data)