from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register/register'),
    path('registersuccess', views.registersuccess, name='register/registersuccess'),
]