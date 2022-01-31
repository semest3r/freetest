from datetime import date, datetime
from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
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

    
class Choice(models.Model):
    nama = models.CharField(max_length=50)
    pilihan = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

class Question(models.Model):
    pertanyaan = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pertanyaan
    
    