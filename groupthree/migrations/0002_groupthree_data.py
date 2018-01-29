# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from groupthree import models

def insert_data_default(apps, schema_editor):
    Juego = apps.get_model('groupthree', 'Juego')
    Juego.objects.create(
        juego_id=2,
        juego='Futbol'
    )

def delete_data_default(apps, schema_editor):
    Juego = apps.get_model('groupthree', 'Juego')
    Juego = Juego.objects.get(
        juego_id=2
    )
    Juego.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('groupthree', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(insert_data_default, delete_data_default)
    ]
