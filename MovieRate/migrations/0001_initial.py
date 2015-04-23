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
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
>>>>>>> 3cab9eeaeae40875ccc08874ebbcd5bb706e8204
                ('user', models.TextField(default='')),
                ('comment_text', models.TextField(default='')),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('like', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
=======
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
>>>>>>> 3cab9eeaeae40875ccc08874ebbcd5bb706e8204
                ('name', models.TextField(default='')),
                ('detail', models.TextField(default='')),
                ('release_date', models.TextField(default='')),
                ('rate', models.FloatField(default=0)),
                ('viewer', models.IntegerField(default=0)),
                ('poster', models.URLField(default='')),
                ('add_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
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
