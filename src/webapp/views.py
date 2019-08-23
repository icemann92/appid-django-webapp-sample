from django.shortcuts import render

import json
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect


def index(request):
    userdata = None

    if request.user.is_authenticated:
        user = request.user
        appIdUser = user.social_auth.get(provider='appid')
        userdata = {
            'user_id': appIdUser.uid,
            'token': appIdUser.access_token
        }

    if userdata is None:
        return render(request, 'webapp/index.html')
    else:
        return render(request, 'webapp/index.html', {
            'userdata': json.dumps(userdata, indent=4)
        })


def logout(request):
    django_logout(request)
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(return_to)
