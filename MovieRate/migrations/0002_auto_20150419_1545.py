# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='add_date',
            field=models.TextField(default=''),
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
