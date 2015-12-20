# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20151213_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, verbose_name=b'Date of Publication', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Title of the Book'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.TextField(max_length=100, verbose_name=b'Main Office Address'),
        ),
    ]
