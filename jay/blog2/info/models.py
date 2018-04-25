from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class Info(models.Model):
    user                  = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key        = models.CharField(max_length=150, blank=True, null=True)
    activated             = models.BooleanField(default=False)
    timestamp             = models.DateTimeField(auto_now_add=True)
    updated               = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{}' .format(self.user, self.username)