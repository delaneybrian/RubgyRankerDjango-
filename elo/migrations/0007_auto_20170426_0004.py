# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0006_remove_team_week_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='awayteam_rating_after',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='hometeam_rating_after',
            field=models.IntegerField(default=0),
        ),
    ]