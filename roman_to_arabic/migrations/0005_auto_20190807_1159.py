# Generated by Django 2.2.4 on 2019-08-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roman_to_arabic', '0004_auto_20190807_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairs',
            name='roman',
            field=models.CharField(max_length=5),
        ),
    ]