from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.views import View
from .forms import PostForm


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': post}

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'posts': post}

    return render(request, 'post_detail.html', context)


class Post_New(View):
    form_user = PostForm

    def get(self, request):
        form = self.form_user(None)
        context = {'forms': form}

        return render(request, 'post_new.html', context)

    def post(self, request):
        form = self.form_user(request.POST)
        context = {'forms': form}

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('/')
        else:
            return render(request, 'post_new.html', context)


class Post_Edit(View):
    form_user = PostForm
    posts_object = Post

    def get(self, request, pk):
        posts = self.posts_object.objects.get(pk=pk)
        form = self.form_user(instance=posts)                       # Передача данных для редактирования

        context = {'forms': form}
        return render(request, 'post_new.html', context)

    def post(self, request, pk):
        posts = self.posts_object.objects.get(pk=pk)

        form = self.form_user(request.POST, instance=posts)         # Передача данных для редактирования
        context = {'forms': form}

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
        else:
            return render(request, 'post_new.html', context)

