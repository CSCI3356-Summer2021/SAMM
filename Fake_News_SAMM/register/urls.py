from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.register, name='register/register'), 
    path('', views.login, name='register/login'),

]
