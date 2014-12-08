# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presenteds', '0002_auto_20141207_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='file',
            field=models.FileField(null=True, upload_to=b'presentations/', blank=True),
            preserve_default=True,
        ),
    ]
