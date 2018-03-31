from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    text = models.TextField()
    room = models.CharField(max_length=100)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text