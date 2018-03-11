# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20180306_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name=b'college',
        ),
        migrations.RemoveField(
            model_name='module',
            name=b'university',
        ),
        migrations.AddField(
            model_name='college',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.University'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='college',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.College'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(default='College of Science and Engineering', max_length=255),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(default='Computing Science 1P', max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='Computing Science', max_length=255),
        ),
    ]