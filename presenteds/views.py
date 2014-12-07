from django.shortcuts import render
from models import UserProfile
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from presenteds.models import UserProfile, Presentation, Comment


def index(request):
    return render(request, 'index.html', {'presentations':Presentation.objects.all().reverse()[:10]})


def profile(request, user_id=None):
    user_profile = UserProfile.objects.get(pk=user_id)
    return render(request, 'profile.html',{'user_profile': user_profile, 'profile_user': user_profile.user,
                                           'presentations':user_profile.user.presentation_set.all()})


def detail(request, p_id=None):
    presented = Presentation.objects.get(pk=p_id)
    presented.view_count += 1
    presented.save()
    owner = presented.owner
    owner_profile = UserProfile.objects.get(user=owner)
    return render(request, 'detail.html', {'presented': presented, 'owner': owner, 'owner_profile':owner_profile,
                                           'comments':presented.comment_set.all()})


def comment(request):
    text = request.POST['text']
    slide = request.POST['slide']
    presentation = request.POST['presented']
    comment = Comment(text=text, owner=request.user, to=Presentation.objects.get(pk=presentation), slide=slide)
    try:
        comment.save()
        return HttpResponse("true")
    except Exception as e:
        return HttpResponse(e.message)


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