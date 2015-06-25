# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Imi\u0119')),
                ('age', models.IntegerField(verbose_name='Wiek')),
                ('height', models.IntegerField(verbose_name='Wysoko\u015b\u0107')),
                ('weight', models.IntegerField(verbose_name='Waga')),
                ('destiny_points', models.IntegerField(verbose_name='Punkty przeznaczenia')),
                ('xp_points', models.IntegerField(verbose_name='Punkty do\u015bwiadczenia')),
                ('factor_build', models.IntegerField(verbose_name='Budowa')),
                ('factor_toughness', models.IntegerField(verbose_name='Wytrzyma\u0142o\u015b\u0107')),
                ('factor_dexterity', models.IntegerField(verbose_name='Zr\u0119czno\u015b\u0107')),
                ('factor_perception', models.IntegerField(verbose_name='Percepcja')),
                ('factor_smartness', models.IntegerField(verbose_name='Spryt')),
                ('factor_character', models.IntegerField(verbose_name='Charakter')),
                ('penalty_days_of_hunger', models.IntegerField(default=0, verbose_name='Kara za g\u0142\xf3d')),
                ('penalty_days_of_thirst', models.IntegerField(default=0, verbose_name='Kara za pragnienie')),
                ('penalty_sickness_chance', models.CharField(default=1, max_length=2, verbose_name='Szansa na zachorowanie', choices=[(1, b'1%'), (5, b'5%')])),
            ],
            options={
                'db_table': 'character_sheets',
                'verbose_name': 'Karta postaci',
                'verbose_name_plural': 'Karty postaci',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('level', models.IntegerField(default=0, verbose_name='Poziom')),
                ('based_on', models.CharField(max_length=255, verbose_name='Bazuje na')),
                ('character', models.ForeignKey(to='character.CharacterSheet')),
            ],
            options={
                'db_table': 'skills',
                'verbose_name': 'Umiej\u0119tno\u015b\u0107',
                'verbose_name_plural': 'Umiej\u0119tno\u015bci',
            },
        ),
        migrations.CreateModel(
            name='Wound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(default=b'light', max_length=10, verbose_name='Wielko\u015b\u0107 rany', choices=[(b'heavy', 'Ci\u0119\u017cka'), (b'light', 'Lekka'), (b'scrape', 'Dra\u015bni\u0119cie')])),
                ('was_treated', models.BooleanField(default=False, verbose_name='by\u0142a opatrzona')),
                ('character', models.ForeignKey(verbose_name='Posta\u0107 kt\xf3ra otrzyma\u0142a ran\u0119', to='character.CharacterSheet')),
            ],
            options={
                'db_table': 'wounds',
                'verbose_name': 'Rana',
                'verbose_name_plural': 'Rany',
            },
        ),
    ]
