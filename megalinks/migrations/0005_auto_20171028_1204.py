# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 06:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megalinks', '0004_auto_20170303_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True, null='True'),
        ),
        migrations.AlterField(
            model_name='link',
            name='tag',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Game', 'Game'), ('TV', 'TV'), ('Tutorial', 'Tutorial'), ('Music', 'Music'), ('Ebook', 'Ebook'), ('Software', 'Software')], default='', max_length=50),
        ),
    ]