# Generated by Django 3.1.5 on 2021-01-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_info_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='username',
        ),
    ]
