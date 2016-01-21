from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Shorted(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=100)
    user = models.ForeignKey(User)
