from dataclasses import field
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *


class LoginView(TemplateView):
    model = User
    template_name = 'html/login.html'

class DashboardView(ListView):
    model = {"Choice": Choice, 
            "Question": Question,}
    template_name = 'html/dashboard.html'

def dashboard(request):
    question1 = Question.objects.all()
    choice = Choice.objects.all()
    print(choice)

    context = {
        'choice': choice,
        'question1' : question1
    }
    return render(request, 'html/dashboard.html', context)
