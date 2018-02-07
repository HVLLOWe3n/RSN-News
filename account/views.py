from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.base import View
from django.utils.translation import gettext_lazy

from .forms import UserForm


class Sing_Up(View):
    form_user = UserForm

    def get(self, request):
        form = self.form_user(None)
        context = {'form': form}

        return render(request, 'SignUp.html', context)

    def post(self, request):
        form = self.form_user(request.POST)
        context = {'form': form}

        if form.is_valid():
            user = form.save(commit=False)

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            user.set_password(password)

            user = authenticate(username=username, email=email, password=password)

            if user is not None:
                if user.is_active:
                    print('Point Two')
                    login(request, user)

                    return gettext_lazy('/')

        return render(request, 'SignUp.html', context)
