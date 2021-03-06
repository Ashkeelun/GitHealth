# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=250)),
                ('last_commit', models.CharField(max_length=150, unique=True)),
                ('parent_dir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_dirs', to='health.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('extension', models.CharField(max_length=15)),
                ('url', models.URLField(max_length=250)),
                ('last_commit', models.CharField(max_length=150, unique=True)),
                ('mlc_size', models.IntegerField()),
                ('mlc_num', models.IntegerField()),
                ('slc_size', models.IntegerField()),
                ('slc_num', models.IntegerField()),
                ('comt_size', models.IntegerField()),
                ('code_size', models.IntegerField()),
                ('parent_dir', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_files', to='health.Directory')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=250)),
                ('last_commit', models.CharField(max_length=150, unique=True)),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repository', to='health.Directory')),
            ],
        ),
    ]
