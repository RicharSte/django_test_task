# Generated by Django 3.1.5 on 2021-01-10 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210111_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_info',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
