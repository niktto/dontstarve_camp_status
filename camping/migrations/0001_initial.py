# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('security', models.CharField(max_length=3, verbose_name='Bezpiecze\u0144stwo obozu', choices=[(b'-3', '-3 - ob\xf3z na dnie w\u0105wozu'), (b'-2', '-2'), (b'-1', '-1'), (b'0', '0 - polana w lesie'), (b'1', '1'), (b'2', '2'), (b'3', '3 - opuszczona fortyfikacja na wzniesieniu')])),
                ('visibility', models.IntegerField(verbose_name='Widoczno\u015b\u0107 obozu', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('amount_of_water_stored', models.DecimalField(verbose_name='Jednostki zebranej wody', max_digits=4, decimal_places=1)),
                ('amount_of_food_stored', models.DecimalField(verbose_name='Jednostki zebranego jedzenia', max_digits=4, decimal_places=1)),
                ('has_food_utensils', models.BooleanField(default=False, verbose_name='Utensylia do gotowania')),
                ('has_clean_clothes', models.BooleanField(default=False, verbose_name='Czyste ubrania')),
                ('has_real_beds', models.BooleanField(default=False, verbose_name='\u0141\xf3\u017cka')),
                ('has_storage', models.BooleanField(default=False, verbose_name='Przestrze\u0144 magazynowa')),
            ],
            options={
                'verbose_name': 'Ob\xf3z',
                'verbose_name_plural': 'Obozy',
            },
        ),
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Imi\u0119')),
                ('amount_of_water_needed', models.DecimalField(default=4, verbose_name='Jednostki dziennie zu\u017cytej wody', max_digits=4, decimal_places=1)),
                ('amount_of_food_needed', models.DecimalField(default=1, verbose_name='Jednostki dziennie zu\u017cytego jedzenia', max_digits=4, decimal_places=1)),
            ],
            options={
                'verbose_name': 'Obozowicz',
                'verbose_name_plural': 'Obozowicze',
            },
        ),
        migrations.AddField(
            model_name='camp',
            name='campers',
            field=models.ManyToManyField(to='camping.Camper'),
        ),
    ]
