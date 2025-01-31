from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", views.login, name="nicelogin"),
    path("ailogin", views.ailogin, name="ailogin"),
    path("authenticate/", views.login_user, name="authenticate"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("new_user/", views.register_user, name="register_user") 
]
