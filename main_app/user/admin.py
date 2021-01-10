from django.contrib import admin

from .models import User_info

#регистрируем приложение в админке
admin.site.register(User_info)