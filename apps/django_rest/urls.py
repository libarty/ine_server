from django.urls import path, include
from . import views

# id for get function
app_name = 'api'
urlpatterns = [
	path('user/', views.UserViewSet.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
	})),
	path('user/<int:pk>', views.UserViewSet.as_view({
		'get_queryset': 'get_queryset',
		'get': 'retrieve',
	})),

	path('already_ip/post/', views.AlreadyIpViewPost.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
		'post': 'create',
	})),
	path('already_ip/get/', views.AlreadyIpViewGet.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
	})),

	path('extra_user/get/', views.ExtraUserViewGet.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
	})),
	path('extra_user/post/', views.ExtraUserViewPost.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
		'post': 'create',
	})),


	path('thought_user/', views.ThoughtUserViewSet.as_view({
		'get': 'list',
		'get_queryset': 'get_queryset',
		'post': 'create',
	})),
	path('thought_user/<int:pk>', views.ThoughtUserViewSet.as_view({
		'get_queryset': 'get_queryset',
		'put': 'update',
		'get': 'retrieve',
		'delete': 'destroy',
	})),
	# for user enter with token
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.authtoken')),
	path('auth/', include('djoser.urls.jwt')),
]
