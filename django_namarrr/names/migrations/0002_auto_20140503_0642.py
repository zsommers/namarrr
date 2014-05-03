# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surname',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noun',
            name='downvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noun',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='surname',
            name='weight',
            field=models.DecimalField(decimal_places=31, default=5, max_digits=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noun',
            name='weight',
            field=models.DecimalField(decimal_places=31, default=5, max_digits=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='surname',
            name='downvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noun',
            name='text',
            field=models.CharField(max_length=64, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surname',
            name='text',
            field=models.CharField(max_length=64, default='bob'),
            preserve_default=False,
        ),
    ]
