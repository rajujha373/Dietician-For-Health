# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20170807_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
