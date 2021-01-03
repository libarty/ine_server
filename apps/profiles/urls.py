from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views




# id for get function
app_name = 'profiles'
urlpatterns = [
	path('login/', views.login, name='login'),
	path('<int:user_id>/', views.profile_page, name = 'profile_page'),
	path('<int:user_id>/add_think/', views.add_think, name = 'add_think'), # add think
	path('<int:page_id>/<int:think_id>/add_com_think/', views.add_com_think, name = 'add_com_think'), # add comment to think
	path('<int:think_id>/delete_think/', views.delete_think, name = 'delete_think'), # delete think
	path('<int:think_com_id>/delete_com_think/', views.delete_com_think, name = 'delete_com_think'), # delete think comment
	
	
	
	#path('done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name = 'password_reset_done'),
	#path('dones/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name = 'password_reset_complete'),
	
	path('change_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='change_password.html'), name = 'change_password'), # chenge password
	
	path('<int:user_id>/change_user/', views.change_user, name = 'change_user'), # change user
]






