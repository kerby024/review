# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0001_initial'),
        ('review_app', '0003_auto_20171204_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='names', to='logreg_app.User'),
            preserve_default=False,
        ),
    ]
