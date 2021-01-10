from django.contrib import admin

from .models import Book_info

#регистрируем приложение в админке
admin.site.register(Book_info)