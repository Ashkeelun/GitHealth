# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20170415_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='last_commit',
        ),
    ]
