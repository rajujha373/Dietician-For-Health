# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_socialnetwork_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(max_length=1000)),
                ('package1_name', models.CharField(max_length=1000)),
                ('package1_img', models.FileField(upload_to='')),
                ('package2_name', models.CharField(max_length=1000)),
                ('package2_img', models.FileField(upload_to='')),
                ('package3_name', models.CharField(max_length=1000)),
                ('package3_img', models.FileField(upload_to='')),
                ('package4_name', models.CharField(max_length=1000)),
                ('package4_img', models.FileField(upload_to='')),
                ('banner_tagline', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Banner Package',
                'verbose_name_plural': 'Banner Packages',
            },
        ),
    ]
