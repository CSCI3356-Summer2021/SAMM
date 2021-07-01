from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import Twitter,Comment
from register.models import User
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def savecontent(request):
    id = request.user.id
    print(id)
    user = User.objects.get(id=id)
    content = request.POST.get('content')
    pic = request.FILES.get('imagefile', '')
    print(pic)
    time =  timezone.now()
    Twitter(uid=id,username=user.username,avatar=user.profile_pic,fav=0,comment=0,zhuan=0,content=content,pic=pic,add_time=time).save()

    return HttpResponse("<script>alert('post success');location.href='/home/'</script>")

def ajaxaddfav(request):
    id = request.POST.get('id')
    tw = Twitter.objects.get(id=id)
    tw.fav = tw.fav+1;
    tw.save();
    return JsonResponse({'count':tw.fav})

def ajaxrepost(request):
    uid = request.user.id
    user = User.objects.get(id=uid)
    id = request.POST.get('id')
    tw = Twitter.objects.get(id=id)
    tw.zhuan = tw.zhuan+1;
    tw.save();
    time =  timezone.now()
    Twitter(uid=uid,username=user.username,avatar=user.profile_pic,fav=0,comment=0,zhuan=0,content=user.username+" re-sended this message: "+tw.content,pic=tw.pic,add_time=time).save()

    return JsonResponse({'count':tw.zhuan})

def ajaxcomment(request):
    uid = request.user.id
    user = User.objec
    id = request.POST.get('id')
    content = request.POST.get('content','')
    tw = Twitter.objects.get(id=id)
    tw.comment = tw.comment+1;
    tw.save(); 

    time =  timezone.now()
    Comment(uid=uid,username=user.username,avatar=user.profile_pic,content=content,add_time=time,tid_id=id).save()

    return JsonResponse({'status':1}) 
