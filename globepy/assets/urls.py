from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all_assets, name='list_all_assets'),
    path('listall/', views.list_all_assets, name='list_all_assets'),
    path('asset-details/<int:id>/', views.assetdetails, name='asset-details'),
    path('create-page/', views.create_page, name='create-new-page'),
    path('updated-compliance-requirement/<int:id>', views.update_compliance_requirement, name='update-compliance-requirement' ),
    path('create-compliance-requirement/<int:frameworkid>/<int:assetid>/<int:requirementid>', views.create_compliance_requirement, name='create-compliance-requirement' ),
    path('comments/add/<int:assetid>/', views.add_comment, name='add_comment'),
    path('comments/add/<int:assetid>/<int:parent_id>/', views.add_comment, name='add_reply'),
    path('comments/delete/<int:assetid>/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comments/update/<int:comment_id>/', views.update_comment, name='update_comment')
    
]

