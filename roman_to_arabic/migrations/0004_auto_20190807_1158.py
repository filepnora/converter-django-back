# Generated by Django 2.2.4 on 2019-08-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roman_to_arabic', '0003_auto_20190807_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairs',
            name='arabic',
            field=models.IntegerField(),
        ),
    ]
