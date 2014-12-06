from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=255)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    title = models.CharField(max_length=255)
    country = CountryField()
    avatar = models.URLField(null=True, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Presentation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    next = models.ForeignKey('self', null=True, blank=True)

    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    owner = models.ForeignKey(User)
    to = models.ForeignKey(Presentation)

    slide = models.PositiveSmallIntegerField()
    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)