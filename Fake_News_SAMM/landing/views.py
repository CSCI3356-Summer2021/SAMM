from django.shortcuts import render
from register.forms import RegisterForm


def index(request):
    return render(request, 'index.html')


