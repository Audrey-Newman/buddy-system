# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20171104_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
