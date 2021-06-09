from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing/index'),
    path('loginpage', views.loginpage, name='landing/loginpage'),
    path('registerpage', views.registerpage, name='landing/registerpage'),
]