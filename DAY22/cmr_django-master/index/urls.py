from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='index'),
    # path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login, name='login'),
    path('product/', views.product, name='product'),
    path('productdetail/', views.product_detail, name='product-detail'),
]
