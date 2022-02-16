from datetime import date
from tkinter import CASCADE
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Choice(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    checklist = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    