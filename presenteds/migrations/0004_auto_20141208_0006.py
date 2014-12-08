# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presenteds', '0003_presentation_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='category',
            field=models.ForeignKey(blank=True, to='presenteds.Category', null=True),
            preserve_default=True,
        ),
    ]
