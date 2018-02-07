from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import View

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
            user.save()

            user = authenticate(username=username, email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('/')

        return render(request, 'SignUp.html', context)
