from django.shortcuts import render

# Create your views here.


def messaging(request):
    user = request.user
    messaging = render.get_messages(user=user)
    active_direct = None
    directs = None

    if messaging:
        message = messaging[0]
        active_direct = message['user'].username
        directs = render.objects.filter(user=user, recipient= message['user'])
        directs.update(is_read = True)

        for message in messaging:
            if message['user'].username == active_direct:
                message['unread'] = 0
        context = {
            'directs' : directs,
            'messaging' : message,
            'active_direct' : active_direct,
        }
    template = loader.get_template('messaging/messaging.html')



    return render(request, 'messaging.html')

