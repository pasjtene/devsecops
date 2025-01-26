from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardhome, name='dashboard_home'),
    path('editors/', views.formeditors, name='forms-editors'),
    path('create-page/', views.create_page, name='create-new-page')    
]

