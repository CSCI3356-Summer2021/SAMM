from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='landing/index'),
    path('savecontent/', views.savecontent, name='landing/savecontent'),
    path('ajaxaddfav/', views.ajaxaddfav, name='landing/ajaxaddfav'),
    path('ajaxrepost/', views.ajaxrepost, name='landing/ajaxrepost'),
    path('ajaxcomment/', views.ajaxcomment, name='landing/ajaxcomment'),
    
]
