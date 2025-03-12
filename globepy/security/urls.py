from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('iso27001/', views.iso27001_requirements, name='iso27001_requirements'),
]