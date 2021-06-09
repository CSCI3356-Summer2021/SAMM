from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def registerpage(request):
    return render(request, 'registerpage.html')