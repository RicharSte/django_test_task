from django.db import models
from django.contrib.auth.models import User

class Book_info(models.Model):
    #Собираем информацию о книге, которую хочет выставить пользователь
    title = models.CharField(max_length=150, null=False)
    descriptiom = models.TextField(max_length=150, null=False)
    prise = models.IntegerField()
    condition = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images')
    
    #нужно для связи с главной таблицей
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)