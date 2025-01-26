from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login as auth_login, authenticate, logout


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    


def anonymous_required(function=None, redirect_url=None):
    
    #messages.info( "Success already loged In")
    
    if not redirect_url:
        redirect_url='homepage'
        
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )
    
    if function:
        return actual_decorator(function)
    return actual_decorator
    
@anonymous_required
def login(request):
    return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    messages.success(request,"Success you are loged out")
    return redirect('homepage')

def login_user(request):
    response_data = {}
    response_data["METHOD"] = request.method
    
    if request.method == 'POST':
        username = request.POST['email'].replace(' ','').lower()
        password = request.POST['password']
        email = request.POST['email'].replace(' ','').lower()
        
        response_data["username"] = username
        response_data["password"] = password
        response_data["email"] = email
        
        if not User.objects.filter(email=email).exists():
            messages.error(request,"Invalid user credentials for email: {} ".format(email))
            return redirect('nicelogin')
        
        authUser =  authenticate(request, username=email, password=password)
        if authUser is None:
            #auth.login(request, authUser)
            messages.info(request,"Success but you are NOT loged In: {} ".format(email))
            return redirect('nicelogin')
        
        if authUser is not None:
            #auth.login(request, authUser)
            auth_login(request, authUser)
            messages.info(request,"Success you are loged In: {} ".format(email))
            return redirect('homepage')
        
    return redirect('nicelogin')

@anonymous_required
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