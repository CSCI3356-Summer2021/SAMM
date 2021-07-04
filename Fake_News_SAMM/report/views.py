from django.shortcuts import render
from .forms import UserReportForm, MessageReportForm
from .models import UserReport, MessageReport
from landing.models import Twitter
# Create your views here.



def ReportUser(request):
    
    if request.method == "POST":
        form = UserReportForm(request.POST, request.FILES)
        if form.is_valid():
            
            m = UserReport.objects.create()
            m.username = form.cleaned_data['username']
            m.reason = form.cleaned_data['reason']
            m.save()
    else:
        form = UserReportForm()
    twitter_objects = Twitter.objects.all()
    context = {
        'form' : form,
        'twitter_objects' : twitter_objects,
    }    
    return render(request, 'report-user-modal.html', context)

def ReportMessage(request):
    if request.method == "POST":
        form = MessageReportForm(request.POST, request.FILES)
        if form.is_valid():
            m = MessageReport.objects.create()
            m.content = form.cleaned_data['content']
            m.username = form.cleaned_data['username']
            m.reason = form.cleaned_data['reason']
            m.additional = form.cleaned_data['additional']
            m.save()
                
    else:
        form = MessageReportForm()
    return render(request, 'report-message-modal.html', {"form":form})