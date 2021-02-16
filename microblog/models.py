import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    heading = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True,  blank=True)
    post = models.CharField(max_length=2000)
    dat_pub = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE,)
    answer = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return self.answer




