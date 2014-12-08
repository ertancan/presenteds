from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    title = models.CharField(max_length=255)
    country = CountryField()
    avatar = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.user)+"'s profile"


class Presentation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, blank=True)
    file = models.FileField(upload_to='/', null=True, blank=True)

    actions = models.TextField(null=True,blank=True)

    next = models.ForeignKey('self', null=True, blank=True)

    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner) + " - " + self.name


class Comment(models.Model):
    owner = models.ForeignKey(User)
    to = models.ForeignKey(Presentation)

    slide = models.PositiveSmallIntegerField()
    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)


class EvaluationCriterion(models.Model):
    name = models.CharField(max_length=100)


class Evaluation(models.Model):
    evaluater = models.ForeignKey(User)
    presentation = models.ForeignKey(Presentation)

    date = models.DateTimeField(auto_now_add=True)


class CriteriaRelation(models.Model):
    evaluation = models.ForeignKey(Evaluation)
    criterion = models.ForeignKey(EvaluationCriterion)

    point = models.PositiveSmallIntegerField()
