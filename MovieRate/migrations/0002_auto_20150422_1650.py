# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user', models.TextField(default='')),
                ('comment_text', models.TextField(default='')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('like', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(to='MovieRate.Movie', default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='add_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='detail',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.URLField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='viewer',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
