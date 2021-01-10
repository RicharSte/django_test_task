"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#инпортируем нужные модули для работы
from user.views import index, loginPage, get_user_info
from books.views import get_book_info

#Напоминани: проставить имена
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('login/', loginPage),
    path('get-info/', get_user_info),
    path('get-book-info/', get_book_info),
]

#Нужно для коретного сохранения фото
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)