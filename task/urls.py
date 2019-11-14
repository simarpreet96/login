from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
	path('', views.signup, name='signup'),
	path('post_list/', views.post_list, name='post_list'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<pk>/del/', views.post_del, name='post_del'),
	path('active/', views.active, name='active'),
	path('inactive/', views.inactive, name='inactive'),
	path('isactive/', views.isactive, name='isactive'),

    #path('password_reset/', auth_views.password_reset, name='password_reset'),
]
