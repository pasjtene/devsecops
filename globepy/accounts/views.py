from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def login(request):
    return render(request, "auth/login.html")

def register(request):
    if request.method == 'POST':
        username = request.post['username']
        password = request.post['assword']
        
    return render(request, "auth/register.html")

def register_user(request):
    response_data = {}
    response_data["METHOD"] = request.method
    
    if request.method == 'POST':
        username = request.post['username']
        password = request.post['assword']
        
        response_data["username"] = username
        response_data["password"] = password
    return JsonResponse(response_data)
        
    #return render(request, "auth/register.html")