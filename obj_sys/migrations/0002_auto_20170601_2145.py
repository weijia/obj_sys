# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('obj_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ufsobj',
            name='position',
            field=geoposition.fields.GeopositionField(default=None, max_length=42, blank=True),
            preserve_default=False,
        ),
    ]
