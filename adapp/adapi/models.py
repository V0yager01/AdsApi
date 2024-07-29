from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    views = models.IntegerField()
    position = models.IntegerField()

