from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='landing/index'),
    path('loginpage', views.loginpage, name='landing/loginpage'),
    path('loginsuccess', views.loginsuccess, name='landing/loginsuccess'),
]