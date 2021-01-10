from django.db import models
from django.contrib.auth.models import User

class User_info(models.Model):
    #все данные здесь нужны для последующего создания фида
    fullname = models.CharField(max_length=75, default='NONAME', null=False)
    phone_number = models.CharField(max_length=12)
    location = models.CharField(max_length=150)
    
    #этот параметр нужен для связи с основной таблицей пользователей.
    #Его не надо выводить прямо или вообще выводить
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)