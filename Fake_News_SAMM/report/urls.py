from django.urls import path
from . import views


urlpatterns = [
    path('ReportMessage/', views.ReportMessage, name='ReportMessage/report-message-model.html'),
    path('ReportUser/', views.ReportUser, name='ReportUser/report-user-model.html'),
]