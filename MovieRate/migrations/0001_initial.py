# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user', models.TextField(default='')),
                ('comment_text', models.TextField(default='')),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('detail', models.TextField(default='')),
                ('release_date', models.TextField(default='')),
                ('rate', models.FloatField(default=0)),
                ('viewer', models.IntegerField(default=0)),
                ('poster', models.URLField(default='')),
                ('add_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=None, to='MovieRate.Movie'),
        ),
    ]
