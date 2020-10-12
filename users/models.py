from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class EntryPoint(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    remote_address = models.GenericIPAddressField(blank=False)
    country = models.CharField(blank=True, max_length=64)
    city = models.CharField(blank=True, max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return "%s:%s" % (self.user.username, self.remote_address)

    def __str__(self):
        return "%s:%s" % (self.user.username, self.remote_address)
