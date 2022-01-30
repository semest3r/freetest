from datetime import date
from pyexpat import model
from venv import create
from django.shortcuts import render
from .forms import ContactForm
from .models import *


def home(request):
    beritas = Berita.objects.all().order_by('-date')
    context = {
        'beritas': beritas,
    }
    return render(request, 'content/home.html', context)

def content1(request):
    context = {}
    return render(request, 'content/content1.html', context)
    
def content2(request):
    context = {}
    return render(request, 'content/content2.html', context)

def content3(request):
    beritas = Berita.objects.order_by('-date')
    context = {
        'beritas': beritas,
    }
    return render(request, 'content/content3.html', context)

def content4(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    contacts = Contact.objects.all().order_by('date')
    context = {
        'form' : form,
        'contacts' : contacts,
    }
    return render(request, 'content/content4.html', context)

