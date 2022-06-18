from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django import forms

from .models import CustomUser
from .models import CustomUserProfile

import random
import hashlib


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password'
        )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['username'].widget.attrs['data-error'] = 'Пожалуйста введите имя пользователя'
        self.fields['password'].widget.attrs['data-error'] = 'Пожалуйста введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            'age',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл. почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['avatar'].widget.attrs['placeholder'] = 'Выберите картинку для аватара'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        return user


class UpdateForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'password',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл. почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['avatar'].widget.attrs['placeholder'] = 'Выберите изображение'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class CustomUserProfileEditForm(forms.ModelForm):
    GENDER_CHOICES = [('W', 'Ж'),
                      ('M', 'М'),]
    gender = forms.ChoiceField(widget=forms.RadioSelect, required=False, choices=GENDER_CHOICES)
    class Meta:
        model = CustomUserProfile
        fields = ('about_me', 'gender')

    def __init__(self, *args, **kwargs):
        super(CustomUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'gender':
                field.widget.attrs['class'] = 'form-control list-inline'

