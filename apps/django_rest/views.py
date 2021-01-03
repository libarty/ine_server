import sys, os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [base_dir]

from django_filters.rest_framework import DjangoFilterBackend



from django.contrib.auth.models import User
# import my models
from profiles.models import *
from pages.models import *
from posts.models import *

# import my serializers

from .serializers import *

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions  # for check user rules
#
# Create your views here.

class ThoughtUserViewSet(viewsets.ModelViewSet):
	serializer_class = ThoughtUserSerializer
	#permission_classes = [permissions.IsAuthenticated]
	queryset = ThoughtUser.objects.all()


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend,]
	filterset_fields = ['email', 'username']
	#permission_classes = [permissions.IsAuthenticated]
	queryset = User.objects.all()

class AlreadyIpViewGet(viewsets.ModelViewSet):
	serializer_class = AlreadyIpSerializer
	filter_backends = [DjangoFilterBackend,]
	filterset_fields = ['ip_name', 'id']
	#permission_classes = [permissions.IsAuthenticated]
	queryset = AlreadyIp.objects.all()

class AlreadyIpViewPost(viewsets.ModelViewSet):
	serializer_class = AlreadyIpSerializer
	permission_classes = [permissions.IsAuthenticated]
	queryset = AlreadyIp.objects.all()

class ExtraUserViewGet(viewsets.ModelViewSet):
	serializer_class = ExtraUserSerializer
	filter_backends = [DjangoFilterBackend,]
	filterset_fields = ['phone', 'id']
	queryset = ExtraUser.objects.all()

class ExtraUserViewPost(viewsets.ModelViewSet):
	serializer_class = ExtraUserSerializer
	#permission_classes = [permissions.IsAuthenticated]
	queryset = ExtraUser.objects.all()