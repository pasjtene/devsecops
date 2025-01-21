from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect


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
    