from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#User creation form automatically includes username, password
class RegisterForm(UserCreationForm): #all same properties as user creation form plus those specified below
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    email = forms.EmailField()

    def clean_email(self): #This function is used to limit email domain to that of bc.edu
        data = self.cleaned_data['email'] #data is that of the input for email
        if "@bc.edu" not in data: #If its not a BC email...
            raise forms.ValidationError("Must be a Boston College email address") #There is a validation error
        return data

    class Meta: #Since we made some changes, this sets the order of the fields in the form
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]
