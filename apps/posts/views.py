from django.shortcuts import render

# load models
from . models import *
from profiles.models import *


def search(request):
	args = {}
	return render(request, 'posts.html', {'args':args }) 
	
	
	
def post_page(request,post_id):
	args = {}
	return render(request, 'posts.html', {'args':args }) 