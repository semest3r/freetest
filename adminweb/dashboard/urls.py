
from unicodedata import name
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard1/', views.dashboard, name='dashboard'),
]
