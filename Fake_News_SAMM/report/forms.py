from django import forms
from .models import UserReport, MessageReport
from django.forms import TextInput

class UserReportForm(forms.ModelForm):
    class Meta:
        model=UserReport
        fields=["username","reason"]
        widgets = {
            'reason' : TextInput(attrs={

                'placeholder' : 'Reason for report...',
                'size' : '50',
            }),
        }
        labels = {
            'reason' : 'Reason for report?'
        }


class MessageReportForm(forms.ModelForm):
    class Meta:
        model=MessageReport
        fields=["content","username","reason","additional"]
        widgets = {

        }
        labels = {
            'reason' : 'Reason for report?'
        }