from django.shortcuts import render, redirect
from .forms import RegisterForm, EditForm
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
            m.bio = form.cleaned_data['bio']
            m.save()
            form.save()
            # fix
            user = User.objects.get(id=m.id)
            user.user_id = m.id
            user.save()

            username = form.cleaned_data.get('username') #Defines username as the username the user input
            messages.info(request, "Welcome " + username + "!") #This displays username as a message
            
            #time.sleep(5) #Delay so message is shown/seen
            #return redirect("/home") #redirect after 5 seconds to homepage
    else:
        form = RegisterForm() #blank form

    return render(request, "register.html", {"form":form})

def login(request):
    return render(request, "login.html")


def editprofile(request, *args, **kwargs):
    user_id = kwargs.get("user_id")
    
    try:
        account = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        acount = None
    if request.method == "POST": 
        
        form = EditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid(): #if form is valid, it saves it to user database
            
            #m = User.objects.get()
            #m.fullname = form.cleaned_data['fullname']
        # m.phone = form.cleaned_data['phone']
            #m.address = form.cleaned_data['address']
            #m.save(request.user)
            form.save()
    else:
        form = EditForm() #blank form
    return render(request, "editprofile.html", {"form":form})
    
        
