from django.shortcuts import render
from models import UserProfile
from django.contrib import auth
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def profile(request, user_id=None):
    user_profile = UserProfile.objects.get(pk=user_id)
    return render(request, 'profile.html',{'user_profile': user_profile, 'profile_user': user_profile.user})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponse("true")
        else:
            return HttpResponse("disabled")
    else:
        return HttpResponse("false")


def logout_view(request):
    auth.logout(request)
    return HttpResponse("true")