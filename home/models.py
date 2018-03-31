from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class GlMsg(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_pk  = models.IntegerField(default=0)
    user_send = models.IntegerField(default=0)

    def __str__(self):
        return str(self.created)

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        user_2, created = cls.objects.get_or_create(
            current_user=new_friend
        )
        user_2.users.add(current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        user_2, created = cls.objects.get_or_create(
            current_user=new_friend
        )
        user_2.users.remove(current_user)
        friend.users.remove(new_friend)
