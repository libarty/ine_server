from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
	path('', views.search, name = 'index' ),
	path('<int:post_id>/', views.post_page, name = 'post_page'),
]