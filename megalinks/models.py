from django.db import models
import datetime
from django.contrib.auth.models import User

class Link(models.Model):
    title = models.CharField(max_length=200, default="")
    date = models.DateTimeField(default=datetime.datetime.now)
    TAG_CHOICES = (
    ("Movie", "Movie"),
    ("Game", "Game"),
    ("TV", "TV"),
    ("Tutorial", "Tutorial"),
    ("Music", "Music"),
    ("Ebook", "Ebook"),
    ("Software", "Software"),
    ("Documentary", "Documentary")
    )
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default="")
    link = models.CharField(max_length=200, default="")
    description = models.TextField(null="True", blank=True)
    size = models.CharField(max_length=10, default="")
    user = models.ForeignKey(User, related_name='user', default=1)

    def __str__(self):
        return self.title

class Account(models.Model):
    user = models.ForeignKey(User, default=1)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
        return self.email


