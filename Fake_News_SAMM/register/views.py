from django.shortcuts import render, redirect
from .forms import RegisterForm
import time
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST": #links to html file, which has method set to POST
        form = RegisterForm(request.POST) #Register form is the form I outline in forms.py
        if form.is_valid(): #if form is valid, it saves it to user database
            form.save()
            username = form.cleaned_data.get('username') #Defines username as the username the user input
            messages.info(request, "Welcome " + username) #This displays username as a message
            
        #time.sleep(5) #Delay so message is shown/seen
        #return redirect("/home") #redirect after 5 seconds to homepage
    else:
        form = RegisterForm() #blank form

    return render(request, "register.html", {"form":form})


def login(request):
    return render(request, 'login.html')