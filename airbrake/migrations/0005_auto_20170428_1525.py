# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airbrake', '0004_auto_20161229_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=128)),
                ('file_line_column', models.TextField()),
                ('notes', models.TextField()),
                ('status', models.CharField(choices=[(b'new', b'new'), (b'resolved', b'resolved'), (b'watching', b'watching')], default=b'new', max_length=16)),
            ],
            options={
                'ordering': ('-modified',),
            },
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=64)),
                ('os', models.CharField(blank=True, max_length=64, null=True)),
                ('dist', models.CharField(blank=True, max_length=64, null=True)),
                ('string', models.TextField(help_text=b'The useragent string that generated this entry.')),
            ],
            options={
                'ordering': ('browser', 'os'),
            },
        ),
        migrations.AddField(
            model_name='errorgroup',
            name='useragents',
            field=models.ManyToManyField(to='airbrake.UserAgent'),
        ),
        migrations.AddField(
            model_name='jserror',
            name='errorgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airbrake.ErrorGroup'),
        ),
    ]
