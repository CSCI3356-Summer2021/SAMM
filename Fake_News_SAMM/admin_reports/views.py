from django.shortcuts import render

# Create your views here.

def admin_reports(request):
    return render(request, 'adminView.html')