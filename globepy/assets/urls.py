from django.urls import path
from . import views

urlpatterns = [
    path('', views.productshome, name='products_home'),
    path('editors/', views.formeditors, name='forms-editors'),
    path('create-page/', views.create_page, name='create-new-page')    
]

