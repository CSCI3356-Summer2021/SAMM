from django.shortcuts import render

# Create your views here.

def ReportMessage(request):
    return render(request, 'report-message-modal.html')

def ReportUser(request):
    return render(request, 'report-user-modal.html')