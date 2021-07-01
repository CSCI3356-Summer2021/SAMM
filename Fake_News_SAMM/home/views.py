from django.shortcuts import render
from register.models import User
from landing.models import Twitter
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
@login_required
def home(request):

    username = request.user.username
    id = request.user.id
    print(id)
    print(username)
    user = User.objects.get(id=id)
    print("user")
    print(user.profile_pic)
    profile_pic = user.profile_pic;

    search = request.GET.get('search',"")
    if search:
        pre = search[0:1]
        if pre == '@':
            user = search[1:]
            list = Twitter.objects.filter(username=user)
        else:
            list = Twitter.objects.filter(content__icontains=search)

    else:
        list = Twitter.objects.all()

    data = []
    import time
    for item in list:
        get_children = []
        for c in item.get_children:
            get_children.append({'username':c.username,'content':c.content,'date':c.add_time.strftime('%Y-%m-%d %H:%M:%S')})

        data.append({
            'id':item.id,
            'author':item.username,
            'image':item.pic.url if item.pic else "",
            'avatar':item.avatar,
            'date':item.add_time.strftime('%Y-%m-%d %H:%M:%S') ,
            'content':item.content,
            'like_count':item.fav,
            'comment_count':item.comment,
            'repost_count':item.zhuan,
            'get_children':get_children
        })
    list = json.dumps(data)
    return render(request, 'homepage.html',locals())



