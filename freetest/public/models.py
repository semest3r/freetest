from datetime import date, datetime
from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Contact(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("base/base.html")
    

class Berita(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    tumbnail = models.ImageField(upload_to='berita', default='default.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    