# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presenteds', '0004_auto_20141208_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='actions',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presentation',
            name='file',
            field=models.FileField(null=True, upload_to=b'/', blank=True),
            preserve_default=True,
        ),
    ]
