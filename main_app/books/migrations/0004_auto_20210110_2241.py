# Generated by Django 3.1.5 on 2021-01-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210110_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_info',
            name='photo',
            field=models.ImageField(upload_to='users/%Y/%m/%d/'),
        ),
    ]
