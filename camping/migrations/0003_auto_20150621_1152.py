# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0002_auto_20150621_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='amount_of_food_stored',
            field=models.DecimalField(verbose_name='Jednostki zebranego jedzenia', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='camp',
            name='amount_of_water_stored',
            field=models.DecimalField(verbose_name='Jednostki zebranej wody', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='daypassedlog',
            name='food_used',
            field=models.DecimalField(verbose_name='Jednostki zu\u017cytego jedzenia', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='daypassedlog',
            name='water_used',
            field=models.DecimalField(verbose_name='Jednostki zu\u017cytej wody', max_digits=8, decimal_places=2),
        ),
    ]
