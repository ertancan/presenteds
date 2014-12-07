# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presenteds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.PositiveSmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('evaluater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('presentation', models.ForeignKey(to='presenteds.Presentation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvaluationCriterion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='criteriarelation',
            name='criterion',
            field=models.ForeignKey(to='presenteds.EvaluationCriterion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='criteriarelation',
            name='evaluation',
            field=models.ForeignKey(to='presenteds.Evaluation'),
            preserve_default=True,
        ),
    ]
