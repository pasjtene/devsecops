from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dashboard_home, name='dashboard_home'),
    path('hello2/', views.say_hello2),
    path('hello3/', views.say_hello3),
    path('hello4/', views.say_hello4)
]

