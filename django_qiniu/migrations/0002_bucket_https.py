# -*- coding: UTF-8 -*-
# Generated by Django 2.2.6 on 2019-11-06 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_qiniu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='https',
            field=models.BooleanField(default=True, verbose_name='是否使用https'),
        ),
    ]
