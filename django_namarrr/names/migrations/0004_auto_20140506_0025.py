# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    """Edited to remove then readd model - automigrate fail"""
    dependencies = [
        ('names', '0003_auto_20140503_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surname',
            name='weight',
            field=models.DecimalField(default=5, decimal_places=15, max_digits=16),
        ),
        migrations.AlterField(
            model_name='noun',
            name='weight',
            field=models.DecimalField(default=5, decimal_places=15, max_digits=16),
        ),
        migrations.AlterField(
            model_name='adjective',
            name='weight',
            field=models.DecimalField(default=5, decimal_places=15, max_digits=16),
        ),
        migrations.RemoveField(
            model_name='surname',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='surname',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='adjective',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='adjective',
            name='upvotes',
        ),
        migrations.RemoveField(
            model_name='noun',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='noun',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='surname',
            name='downvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='surname',
            name='upvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adjective',
            name='downvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adjective',
            name='upvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noun',
            name='downvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='noun',
            name='upvotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
