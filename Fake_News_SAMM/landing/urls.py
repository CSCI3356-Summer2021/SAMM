from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing/index'),
    path('login', views.login, name='landing/login'),
    path('register', views.register, name='landing/register'),
]