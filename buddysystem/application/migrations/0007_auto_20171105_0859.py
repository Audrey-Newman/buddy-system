# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_profile_num_companions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='num_companions',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
