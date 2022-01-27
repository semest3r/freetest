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
    