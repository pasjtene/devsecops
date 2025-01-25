from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def formeditors2(request):
    return HttpResponse('LMS --- Hello world...!!! <br/> Another hello world <br> link <a href="/lms/hello2">go to hello2 </a>')

def formeditors(request):
    response_data = {}
    response_data["erro"] = "LMS -- No error found"
    response_data["message"] = "Hello world"
    return render(request, "dashboard/forms-editors.html", {"vars": response_data, "name":"Pascal JT"})

def create_page(request):
    return render(request, "dashboard/create-page.html")

@login_required
def dashboardhome(request):
    response_data = {}
    response_data["erro"] = "LMS -- No error found"
    response_data["message"] = "Hello world"
    return render(request, "dashboard/index.html", {"vars": response_data, "name":"Pascal JT"})

def say_hello3(request):
    return JsonResponse({"response":"Hello world json"})

def say_hello4(request):
    response_data = {}
    response_data["erro"] = "No error found"
    response_data["message"] = "Hello world"
    return JsonResponse(response_data)