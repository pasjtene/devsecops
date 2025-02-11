from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_assets, name='list_all_assets'),
    path('listall/', views.list_all_assets, name='list_all_assets'),
    path('asset-details/<int:id>/', views.assetdetails, name='asset-details'),
    path('create-page/', views.create_page, name='create-new-page'),
    path('updated-compliance-requirement/<int:id>', views.update_compliance_requirement, name='update-compliance-requirement' ),
    path('updated-compliance-requirement/<int:frameworkid>/<int:assetid>/<int:requirementid>', views.create_compliance_requirement, name='create-compliance-requirement' ),
    
    
]

