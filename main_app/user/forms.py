from django import forms
from django.contrib.auth.models import User

from .models import User_info

class LoginForm(forms.ModelForm):
    #простейшая форма для логина
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
        
class User_InfoForm(forms.ModelForm):
    #форма для получения данных для фида
    #Напоминание: есть фалидатор для проверки телефона, его надо использовать
    class Meta:
        model = User_info
        fields = [
            'fullname',
            'phone_number',
            'location'
        ]
