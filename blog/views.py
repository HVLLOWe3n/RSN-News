from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.utils import timezone
from django.views import View
from .forms import PostForm


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {'posts': post}

    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        context = {
            'posts': post,
            'next': post.pk + 1,
            'prev': post.pk - 1,
        }

    except Post.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'post_detail.html', context)


class Post_New(View):
    form_user = PostForm

    def get(self, request):
        form = self.form_user(None)
        context = {'form': form}

        return render(request, 'post_new.html', context)

    def post(self, request):
        form = self.form_user(request.POST)
        context = {'form': form}

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('/')
        else:
            return render(request, 'post_new.html', context)


class Post_Edit(UpdateView):
    model = Post
    fields = ['title', 'text']

    template_name = 'post_new.html'

    def get_success_url(self):
        print('')
        return gettext_lazy('/')


class Post_Delete(DeleteView):
    model = Post
    success_url = gettext_lazy('/')


