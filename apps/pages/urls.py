from django.urls import path, include
from . import views

# id for get function
app_name = 'pages'
urlpatterns = [
	path('home/', views.home, name='home'),
	path('404/', views.none, name='none'),
	
	path('add/', views.add, name='add'),
	path('info/', views.info, name='info'),
]

