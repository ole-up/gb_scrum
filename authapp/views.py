from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from django.contrib import auth
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, UpdateForm, CustomUserProfileEditForm
from .models import CustomUser


def login(request: HttpRequest):
    title = {
        "page_title": "Авторизация",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Вход в личный кабинет"
    }

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('personal:main'))
    else:
        form = LoginForm()

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')


def register(request: HttpRequest):
    title = {
        "page_title": "Регистраиция",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Регистрация пользователя"
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('сообщение отправлено')
            else:
                print('ошибка отправки')
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        form = RegisterForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'authapp/register.html', context)


@login_required
@transaction.atomic
def edit_profile(request: HttpRequest):
    title = {
        "page_title": "Личный кабинет",
        "title_row_1": "Наш Хабр",
        "title_row_2": "Ваш профиль"
    }

    if request.method == 'POST':
        user_form = UpdateForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = CustomUserProfileEditForm(data=request.POST, instance=request.user.customuserprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('auth:profile'))

    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = CustomUserProfileEditForm(instance=request.user.customuserprofile)

    context = {
        'title': title,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'authapp/profile.html', context)


def send_verify_mail(user):
    pass


def verify(request: HttpRequest, email, activation_key):
    pass
