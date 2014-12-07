from django.shortcuts import render
from models import UserProfile
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from presenteds.models import UserProfile


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


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    title = request.POST['title']
    country = request.POST['country'].upper()
    try:
        user = User.objects.create_user(username, email, password)
        profile_obj = UserProfile(title=title, country=country, user=user)
        profile_obj.save()
        u = auth.authenticate(username=username, password=password)
        auth.login(request, u)
        return HttpResponse("true")
    except Exception as e:
        return HttpResponse(e.message)


def logout_view(request):
    auth.logout(request)
    return HttpResponse("true")