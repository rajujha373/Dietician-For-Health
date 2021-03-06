# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=1000)),
                ('p1', models.IntegerField(verbose_name='Price for 2 months')),
                ('p2', models.IntegerField(verbose_name='Price for 3 months')),
                ('p3', models.IntegerField(verbose_name='Price for 6 months')),
                ('p4', models.IntegerField(verbose_name='Price for 12 months')),
                ('p5', models.IntegerField(verbose_name='Price for 18 months')),
                ('offer_p1', models.IntegerField(verbose_name='Offer Price for 2 months')),
                ('offer_p2', models.IntegerField(verbose_name='Offer Price for 3 months')),
                ('offer_p3', models.IntegerField(verbose_name='Offer Price for 6 months')),
                ('offer_p4', models.IntegerField(verbose_name='Offer Price for 12 months')),
                ('offer_p5', models.IntegerField(verbose_name='Offer Price for 18 months')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Catagory')),
            ],
        ),
    ]
