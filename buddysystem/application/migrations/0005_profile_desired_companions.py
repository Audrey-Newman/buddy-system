# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_profile_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desired_companions',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]