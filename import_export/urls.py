"""import_export URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # new

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
	path('admin/', admin.site.urls),
	path('log/', include('django.contrib.auth.urls')), # !! Log in and Log out
	path('i18n/', include('django.conf.urls.i18n')), # for multilingual site
	path('api/', include('django_rest.urls')), # api for client

]

# for multilingual site
urlpatterns += i18n_patterns(
	#path('pages/', include('django.contrib.flatpages.urls')),
	# connect my url 
	path('profiles/', include('profiles.urls')),
	path('posts/', include('posts.urls')),
	path('pages/', include('pages.urls')),
)


# DEBUG for file
from django.conf import settings # new
from django.conf.urls.static import static # new

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)