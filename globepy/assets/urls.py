from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_assets, name='list_all_assets'),
    path('listall/', views.list_all_assets, name='list_all_assets'),
    path('asset-details/<int:id>/', views.assetdetails, name='asset-details'),
    path('create-page/', views.create_page, name='create-new-page')    
]

