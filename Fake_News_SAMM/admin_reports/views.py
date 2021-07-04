from django.shortcuts import render
from report.models import UserReport, MessageReport
from django.views.generic.detail import DetailView

# Create your views here.

def admin_reports(request):
    user_objects = UserReport.objects.all()
    message_objects = MessageReport.objects.all()
    context= {
        'user_objects' : user_objects,
        'message_objects' : message_objects,
    }
    return render(request, 'adminView.html', context)