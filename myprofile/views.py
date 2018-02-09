from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Post
from django.utils import timezone


class Profile(View):
    def get(self, request):
        context = {}
        return render(request, 'MyProfilePage.html', context)


class My_Posts(View):
    def get(self, request):
        post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        context = {'post': post}
        return render(request, 'MyAllPosts.html', context)


class None_Post(View):
    def get(self, request):
        context = {}
        return render(request, 'NonePost.html', context)
