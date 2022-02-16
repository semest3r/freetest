from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


def home(request):
    beritas = Berita.objects.all().order_by('-date')
    context = {
        'beritas': beritas,
    }
    return render(request, 'content/home.html', context)

def content1(request):
    form = ChoiceForm()
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid(): 
            form.save()

    choices = Choice.objects.all()
    questions = Question.objects.order_by('id')
    context = {
        'questions' : questions,
        'form' : form,
        'choices' : choices,
        'obj' : obj,
    }
    return render(request, 'content/content1.html', context)
    
def content2(request):
    obj, created = Person.objects.update_or_create(
    first_name='John', last_name='Lennon',
    defaults={'first_name': 'Bob'},
) 

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

