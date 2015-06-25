# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camping', '0004_auto_20150621_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='security',
            field=models.CharField(help_text='Podaj od 1 do 100 (bo to procenty)', max_length=3, verbose_name='Bezpiecze\u0144stwo obozu', choices=[(b'-3', '-3 - ob\xf3z na dnie w\u0105wozu'), (b'-2', '-2'), (b'-1', '-1'), (b'0', '0 - polana w lesie'), (b'1', '1'), (b'2', '2'), (b'3', '3 - opuszczona fortyfikacja na wzniesieniu')]),
        ),
    ]
