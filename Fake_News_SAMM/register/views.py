from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST": #links to html file, which has method set to POST
        form = RegisterForm(request.POST) 
        if form.is_valid(): #if form is valid, it saves it to user database
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm() #blank form

    return render(request, "register.html", {"form":form})

def registersuccess(request):
    return render(request, 'registersuccess.html')