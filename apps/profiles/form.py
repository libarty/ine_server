from django import forms
from django.forms import ModelForm
from . models import *




class ExForm(ModelForm):
	class Meta:
		model = ExtraUser
		fields = ['icon_id', 'back_id', 'icon_colors', 'filter','phone']
		