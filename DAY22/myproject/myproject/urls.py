from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('login/', views.loginhome, name='loginhome'),
    path('register/', views.register, name='register'),
    path('product/', views.product, name='product'),

]