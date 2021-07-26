from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('businesses/', views.businesses, name='businesses'),
    path('neigborhood/', views.neighborhood, name='neighborhood'),
    path('profile/', views.profile, name='profile'),
]