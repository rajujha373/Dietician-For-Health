# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_socialnetwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
