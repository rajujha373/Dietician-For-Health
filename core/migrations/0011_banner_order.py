# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170809_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]