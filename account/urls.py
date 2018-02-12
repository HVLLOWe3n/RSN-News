from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Sing_Up.as_view(), name='sign_up'),
    path('signout/', views.Sign_Out.as_view(), name='sign_out'),
    path('signin/', views.Sign_In.as_view(), name='sign_in'),
    path('about/', views.About.as_view(), name='about'),
]
