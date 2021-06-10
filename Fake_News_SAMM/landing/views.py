from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'loginpage.html')


def loginsuccess(request):
    return render(request, 'loginsuccess.html')

