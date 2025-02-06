from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_assets, name='list_all_assets'),
    path('listall/', views.list_all_assets, name='list_all_assets'),
    path('create-page/', views.create_page, name='create-new-page')    
]

