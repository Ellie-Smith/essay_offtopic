# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170328_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_essay',
            name='content',
            field=models.CharField(default='', max_length=350),
        ),
        migrations.AlterField(
            model_name='user_essay',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='\u4fdd\u5b58\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='user_essay',
            name='isSubmit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_essay',
            name='update_date',
            field=models.DateField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='user_essay',
            name='user_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]