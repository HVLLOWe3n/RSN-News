from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.Post_New.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.Post_Edit.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.Post_Delete.as_view(), name='post_delete'),
]
