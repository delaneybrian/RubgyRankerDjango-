# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0010_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='mainimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='subimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]