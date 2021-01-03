import sys, os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [base_dir]

from django.contrib.auth.models import User
# import my models
from profiles.models import *
from pages.models import *
from posts.models import *

from rest_framework import serializers

# serializers need for show models in rest_framework


class ThoughtUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = ThoughtUser
		fields = (
			'id',
			'connect',
			'title',
			'text',
			'pud_date',
		)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'email',
		)


class AlreadyIpSerializer(serializers.ModelSerializer):
	class Meta:
		model = AlreadyIp
		fields = (
			'id',
			'ip_name',
		)

class ExtraUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExtraUser
		fields = (
			'id',
			'phone',
			'user',
		)





# from django_filters import rest_framework
#
# class CharFilterInFilter(rest_framework.BaseInFilter,rest_framework.CharFilter):
# 	pass
#
# class MovieFilter(rest_framework.FilterSet):
# 	username = CharFilterInFilter(field_name='',lookup_expr='in')
# 	email =
# 	class Meta:
# 		model = User
# 		fields = (
# 			'id',
# 			'username',
# 			'email',
# 		)