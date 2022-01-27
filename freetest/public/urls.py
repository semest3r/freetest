from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('content1/', views.content1, name="content1"),
    path('content2/', views.content2, name="content2"),
    path('content3/', views.content3, name="content3"),
    path('content4/', views.content4, name="content4"),
]
