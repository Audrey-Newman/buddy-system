# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_profile_desired_companions'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='num_companions',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]