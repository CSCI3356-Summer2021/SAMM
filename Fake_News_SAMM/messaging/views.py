from django.shortcuts import render

# Create your views here.

def messaging(request):
    return render(request, 'messaging.html')
