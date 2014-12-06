from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def profile(request, user_id=None):
    return render(request, 'profile.html')