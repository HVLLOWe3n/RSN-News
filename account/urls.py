from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Sing_Up.as_view(), name='sign_up'),
    path('signout/', views.Sign_Out.as_view(), name='sign_out'),
]
