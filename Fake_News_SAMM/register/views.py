from django.shortcuts import render, redirect
from .forms import RegisterForm
import time
from django.contrib import messages
from .models import User

# Create your views here.



def register(request):
    if request.method == "POST": #links to html file, which has method set to POST
        form = RegisterForm(request.POST, request.FILES) #Register form is the form I outline in forms.py
        if form.is_valid(): #if form is valid, it saves it to user database
            #x = form.save(commit=True)
            m = User.objects.create()
            m.username = form.cleaned_data['username']
            m.fullname = form.cleaned_data['fullname']
            m.email = form.cleaned_data['email']
            m.phone = form.cleaned_data['phone']
            m.address = form.cleaned_data['address']
            m.profile_pic = form.cleaned_data['profile_pic']
            m.save()
            form.save()
            username = form.cleaned_data.get('username') #Defines username as the username the user input
            messages.info(request, "Welcome " + username + "!") #This displays username as a message
            
        #time.sleep(5) #Delay so message is shown/seen
        #return redirect("/home") #redirect after 5 seconds to homepage
    else:
        form = RegisterForm() #blank form

    return render(request, "register.html", {"form":form})

def login(request):
    
    return render(request, "login.html")

def editprofile(request):
    
    return render(request, "editrofile.html")