from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


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
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email'].replace(' ','').lower()
        
        response_data["username"] = username
        response_data["password"] = password
        response_data["email"] = email
        
        if not password == password2:
            messages.error(request, "Your two passwords do not match")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"A user with email: {} already exist.".format(email))
            return redirect('register')
        
        newUser =  User.objects.create_user(
           username=username,
            email=email,
            password=password,
            first_name = first_name,
            last_name=last_name
        )
        
        newUser.save()
        auth.login(request, newUser)
        
    #return JsonResponse(response_data)
    return redirect('hello2')
        
    #return render(request, "auth/register.html")