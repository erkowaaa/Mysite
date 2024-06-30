from django.contrib import admin
from .models import *
from modeltranslation.translator import TranslationOptions, register



@register(Task)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'description')