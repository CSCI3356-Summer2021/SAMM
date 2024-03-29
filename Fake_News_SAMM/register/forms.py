from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import EmailInput, TextInput, PasswordInput

#User creation form automatically includes username, password
class RegisterForm(UserCreationForm): #all same properties as user creation form plus those specified below
    fullname = forms.CharField(max_length=200, label ="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    phone = forms.CharField(max_length=200, label ="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    address = forms.CharField(max_length=200, label ="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    bio = forms.CharField(max_length=500, label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bio (Not Required)'}), required=False)
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),
    )
    profile_pic = forms.ImageField()

    def clean_email(self): #This function is used to limit email domain to that of bc.edu
        data = self.cleaned_data['email'] #data is that of the input for email
        if "@bc.edu" not in data: #If its not a BC email...
            raise forms.ValidationError("Must be a Boston College email address") #There is a validation error
        return data

    class Meta: #Since we made some changes, this sets the order of the fields in the form
        model = User
        
        fields = ["username", "fullname", "email", "phone", "address", "password1", "password2", "bio", "profile_pic"]
        widgets = {
            'username' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username',
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }),
        }
        labels = {
            'username' : '',
            'email' : '',
        }

class EditForm(forms.ModelForm):
    fullname = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    bio = forms.CharField(max_length=500)
    
    class Meta:
        model = User
        fields = ["fullname", "phone", "address", "bio"]
    
    def save(self, commit=True):
        account = super(EditForm, self).save(commit=False)
        account.fullname = self.cleaned_data['fullname']
        account.phone = self.cleaned_data['phone']
        account.address = self.cleaned_data['address']
        account.bio = self.cleaned_data['bio']
        if commit:
            account.save()
        return account

