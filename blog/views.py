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


class Post_Detail(View):

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)

            # получение всех id из таблицы Post, 'id' - поле получения записей, flat - получение всех значений в list
            id_list = Post.objects.values_list('id', flat=True)

            if pk != id_list.last():
                next_id = Post.objects.filter(id__gt=pk).first().id  # Получение следуещего id поста для передачи в url

            else:
                next_id = None

            if pk != id_list.first():
                prev_id = Post.objects.filter(id__lt=pk).last().id  # Получение предыдущего id поста для передачи в url

            else:
                prev_id = None

            context = {
                'posts': post,
                'next': next_id,
                'prev': prev_id,
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


