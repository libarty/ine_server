# for translate models

from modeltranslation.translator import register, TranslationOptions
from .models import *

#@register(ThoughtUser)
#class ThoughtUserTranslationOptions(TranslationOptions):
#	fields = ('title','text')