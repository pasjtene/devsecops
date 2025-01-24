from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dashboardhome, name='dashboard_home'),
    
]

