# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-21 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_comments_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_id', to='wall.Messages'),
        ),
    ]
