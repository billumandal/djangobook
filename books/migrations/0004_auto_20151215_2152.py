# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20151213_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='email_address',
            new_name='email',
        ),
    ]
