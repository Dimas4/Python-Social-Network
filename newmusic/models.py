from django.db import models
from django.contrib.auth.models import User

class Files(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    our_file = models.FileField(upload_to='profile_image')
    image = models.ImageField(upload_to='profile_image', blank=True, default='new.jpg')
    data_time = models.DateTimeField(auto_now_add=True)




class Files_sv(models.Model):
    users = models.ManyToManyField(Files)
    current_user = models.ForeignKey(User, related_name='filessv', null=True)

    @classmethod
    def add_files(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )

        friend.users.add(new_friend)

    @classmethod
    def remove_files(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )

        friend.users.remove(new_friend)

