from django.shortcuts import render

# Create your views here.


def home(request):
	args = {}
	return render(request, 'home.html', {'args':args }) 
	
	
	
	
	
def add(request):
	args = {}
	return render(request, 'add.html', {'args':args }) 
	
def info(request):
	args = {}
	return render(request, 'info.html', {'args':args }) 
	
	
	
def none(request):
	args = {}
	return render(request, '404.html', {'args':args }) 