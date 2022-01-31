from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'name', 'comment']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input mx-auto appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder' : 'title'}),
            'name': forms.TextInput(attrs={'class': 'form-input mx-auto appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm', 'placeholder' : 'name'}),
            'comment': forms.Textarea(attrs={'class': 'form-textarea mx-auto rounded appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm','rows':'5', 'placeholder':'your message..'}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice

        fields = ['nama', 'pilihan']

        Widgets = {
            'nama' : forms.TextInput(attrs={'class': 'form-input'}),
            'pilihan' : forms.BooleanField()
        }

class Question(forms.ModelForm):
    class Meta:
        model = Question

        fields = ['pertanyaan']

        widgets = {
            'pertanyaan': forms.TextInput(attrs={'class': 'form-input'})
        }