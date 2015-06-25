# -*- coding: utf-8 -*-
from django.db import models


class CharacterSheet(models.Model):

    class Meta:
        db_table = 'character_sheets'
        verbose_name = u"Karta postaci"
        verbose_name_plural = u"Karty postaci"

    name = models.CharField(u"Imię", max_length=255, unique=True)
    age = models.IntegerField(u"Wiek")
    height = models.IntegerField(u"Wysokość")
    weight = models.IntegerField(u"Waga")
    destiny_points = models.IntegerField(u"Punkty przeznaczenia")

    xp_points = models.IntegerField(u"Punkty doświadczenia")

    # Współczynniki
    factor_build = models.IntegerField(u"Budowa")
    factor_toughness = models.IntegerField(u"Wytrzymałość")
    factor_dexterity = models.IntegerField(u"Zręczność")
    factor_perception = models.IntegerField(u"Percepcja")
    factor_smartness = models.IntegerField(u"Spryt")
    factor_character = models.IntegerField(u"Charakter")

    # Kary
    penalty_days_of_hunger = models.IntegerField(u"Kara za głód", default=0)
    penalty_days_of_thirst = models.IntegerField(
        u"Kara za pragnienie", default=0
    )
    penalty_sickness_chance = models.CharField(
        u"Szansa na zachorowanie",
        choices=(('1', '1%'), ('5', '5%')),
        default='1',
        max_length=2
    )

    def __unicode__(self):
        return u"Karta postaci {}".format(self.name)

    def generate_skills(self):
        names = [
            (u"Survival", ["factor_smartness"]),
            (u"Orientacja w terenie", ["factor_perception"]),
            (u"Leczenie ran", ["factor_smartness"]),
            (u"Skradanie", ["factor_perception"]),
            (u"Sprint", ["factor_toughness"]),
            (u"Pływanie", ["factor_toughness"]),
            (u"Czujność", ["factor_perception"]),
            (u"Niezłomność", ["factor_character"]),
            (u"Cwaniactwo", ["factor_character"]),
            (u"Bijatyka", ["factor_build", "factor_dexterity"]),
            (u"Broń biała", ["factor_build", "factor_dexterity"]),
            (u"Łuki i kusze", ["factor_toughness", "factor_perception"]),
            (u"Broń palna", ["factor_dexterity", "factor_perception"]),
            (u"Broń ciężka", ["factor_build", "factor_toughness"]),
            (u"Rzucanie", ["factor_build", "factor_dexterity"]),
            (u"Zwierzęta", ["factor_character"]),
            (u"Przedwojenny świat", ["factor_smartness"]),
            (u"Mechanika", ["factor_smartness"]),
            (u"Komputery i elektronika", ["factor_smartness"]),
            (u"Nauki ścisłe", ["factor_smartness"]),
            (u"Kierowanie pojazdami", ["factor_smartness"]),
        ]
        for name, bases in names:
            skill = Skill(name=name, character=self)
            skill.set_based_on(bases)
            skill.save()

    def save(self, *args, **kwargs):
        if self.pk is None:
            result = super(CharacterSheet, self).save(*args, **kwargs)
            self.generate_skills()
        else:
            result = super(CharacterSheet, self).save(*args, **kwargs)
        return result


class Wound(models.Model):

    PENALTIES = {
        'scrape': {'treated': 0, 'untreated': 1},
        'light': {'treated': 5, 'untreated': 10},
        'heavy': {'treated': 15, 'untreated': 30},
    }

    SIZES = {
        'scrape': u"Draśnięcie",
        'light': u"Lekka",
        'heavy': u"Ciężka",
    }

    class Meta:
        db_table = 'wounds'
        verbose_name = u"Rana"
        verbose_name_plural = u"Rany"

    size = models.CharField(
        verbose_name=u"Wielkość rany",
        choices=SIZES.items(),
        default='light',
        max_length=10
    )
    was_treated = models.BooleanField(
        verbose_name=u"była opatrzona",
        default=False
    )

    character = models.ForeignKey(
        CharacterSheet,
        verbose_name=u"Postać która otrzymała ranę",
    )

    def __unicode__(self):
        return u"{} rana {} w {}".format(
            u'opatrzona' if self.was_treated else u'wymagająca uwagi',
            self.SIZES[self.size],
            self.character.name
        )

    @property
    def penalty(self):
        return self.PENALTIES[self.size][
            'treated' if self.was_treated else 'untreated'
        ]


class Skill(models.Model):

    class Meta:
        db_table = 'skills'
        verbose_name = u"Umiejętność"
        verbose_name_plural = u"Umiejętności"

    BASES = (
        ("factor_build", u"Budowa"),
        ("factor_dexterity", u"Zręczność"),
        ("factor_perception", u"Percepcja"),
        ("factor_smartness", u"Spryt"),
        ("factor_character", u"Charakter"),
        ("factor_toughness", u"Wytrzymałość"),
    )

    name = models.CharField(u"Nazwa", max_length=255)
    level = models.IntegerField(u"Poziom", default=0)
    based_on = models.CharField(u"Bazuje na", max_length=255)
    character = models.ForeignKey(CharacterSheet)

    def get_based_on(self):
        return self.based_on.split(';')

    def set_based_on(self, bases_list):
        self.based_on = ';'.join(bases_list)

    def get_base_difficulty(self, test_level):
        base_diffs = [
            (getattr(self.character, base) * 5) for base in self.get_based_on()
        ]
        base_diff = sum(base_diffs) / len(base_diffs)

        return base_diff - (10 * test_level) - (10 * self.level)
