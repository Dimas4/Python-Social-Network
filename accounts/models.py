from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)


    london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
