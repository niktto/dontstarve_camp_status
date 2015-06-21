# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayPassedLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('was_found_that_day', models.BooleanField()),
                ('water_used', models.DecimalField(verbose_name='Jednostki zu\u017cytej wody', max_digits=4, decimal_places=1)),
                ('food_used', models.DecimalField(verbose_name='Jednostki zu\u017cytego jedzenia', max_digits=4, decimal_places=1)),
            ],
        ),
        migrations.AddField(
            model_name='camp',
            name='name',
            field=models.CharField(default='Ob\xf3z', max_length=255, verbose_name='Nazwa obozu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='uri',
            field=models.CharField(default='oboz', help_text='Nazwa b\u0105d\u017a fragment nazwy, kt\xf3ry nadaje si\u0119 do umieszczenia w linku do obozowiska. Mo\u017ce by\u0107 inna ni\u017c nazwa obozu.', unique=True, max_length=50, verbose_name='Nazwa w adresie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daypassedlog',
            name='camp',
            field=models.ForeignKey(to='camping.Camp'),
        ),
    ]
