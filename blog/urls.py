from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/(P<pk>/d+)/', views.post_detail, name='post_detail'),
    path('post/new/', views.Post_New.as_view(), name='post_new'),
    path('post/(P<pk>/d+)/edit/', views.Post_Edit.as_view(), name='post_edit'),
]
