# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Translation',
            new_name='Translations',
        ),
    ]