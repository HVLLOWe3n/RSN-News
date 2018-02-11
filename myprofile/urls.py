from django.urls import path
from . import views

urlpatterns = [
    path('myprofile/', views.Profile.as_view(), name='profile'),
    path('myallposts/', views.My_Posts.as_view(), name='myposts'),
]
