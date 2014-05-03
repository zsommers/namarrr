# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_auto_20140503_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjective',
            name='text',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='noun',
            name='text',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='surname',
            name='text',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
