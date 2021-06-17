from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.login, name='landing/login'),
     url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('landing/login/', 'django.contrib.auth.views.login', name='login'),
]

