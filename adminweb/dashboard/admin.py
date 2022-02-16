from django.contrib import admin
from .models import *


admin.site.register(User)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']})]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)