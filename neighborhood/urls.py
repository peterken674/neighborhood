from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('businesses/', views.businesses, name='businesses'),
    path('neigborhood/', views.neighborhood, name='neighborhood'),
    path('profile/', views.profile, name='profile'),
    path('auth/login/', views.login_user, name='login'),
    path('auth/register/', views.register_user, name='register'),
    path('accounts/logout/', views.logout_user, name='logout'),
]