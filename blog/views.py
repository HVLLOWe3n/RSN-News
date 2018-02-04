from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': post}

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'posts': post}

    return render(request, 'post_detail.html', context)
