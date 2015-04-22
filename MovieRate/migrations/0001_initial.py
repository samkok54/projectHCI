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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user', models.TextField(default='')),
                ('comment_text', models.TextField(default='')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('like', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.TextField(default='')),
                ('detail', models.TextField(default='')),
                ('release_date', models.TextField(default='')),
                ('rate', models.FloatField(default=0)),
                ('viewer', models.IntegerField(default=0)),
                ('poster', models.URLField(default='')),
                ('add_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(to='MovieRate.Movie', default=None),
            preserve_default=True,
        ),
    ]
