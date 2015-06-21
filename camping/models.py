# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

from .utils import k100


class Camper(models.Model):

    class Meta:
        verbose_name = u"Obozowicz"
        verbose_name_plural = u"Obozowicze"

    name = models.CharField(verbose_name=u"Imię", max_length=255)

    amount_of_water_needed = models.DecimalField(
        verbose_name=u"Jednostki dziennie zużytej wody",
        decimal_places=1,
        max_digits=4,
        default=4
    )
    amount_of_food_needed = models.DecimalField(
        verbose_name=u"Jednostki dziennie zużytego jedzenia",
        decimal_places=1,
        max_digits=4,
        default=1
    )

    def __unicode__(self):
        return self.name


class Camp(models.Model):

    class Meta:
        verbose_name = u"Obóz"
        verbose_name_plural = u"Obozy"

    name = models.CharField(max_length=255, verbose_name=u"Nazwa obozu")

    uri = models.CharField(
        max_length=50,
        verbose_name=u"Nazwa w adresie",
        help_text=(
            u"Nazwa bądź fragment nazwy, który nadaje się do umieszczenia w "
            u"linku do obozowiska. Może być inna niż nazwa obozu."
        ),
        unique=True
    )

    security = models.CharField(
        verbose_name=u"Bezpieczeństwo obozu",
        choices=(
            ('-3', u'-3 - obóz na dnie wąwozu'),
            ('-2', u'-2'),
            ('-1', u'-1'),
            ('0', u'0 - polana w lesie'),
            ('1', u'1'),
            ('2', u'2'),
            ('3', u'3 - opuszczona fortyfikacja na wzniesieniu'),
        ),
        max_length=3
    )
    visibility = models.IntegerField(
        verbose_name=u"Widoczność obozu",
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    amount_of_water_stored = models.DecimalField(
        verbose_name=u"Jednostki zebranej wody",
        decimal_places=2,
        max_digits=8
    )
    amount_of_food_stored = models.DecimalField(
        verbose_name=u"Jednostki zebranego jedzenia",
        decimal_places=2,
        max_digits=8
    )

    has_food_utensils = models.BooleanField(verbose_name=u"Utensylia do gotowania", default=False)
    has_clean_clothes = models.BooleanField(verbose_name=u"Czyste ubrania", default=False)
    has_real_beds = models.BooleanField(verbose_name=u"Łóżka", default=False)
    has_storage = models.BooleanField(verbose_name=u"Przestrzeń magazynowa", default=False)

    campers = models.ManyToManyField(Camper)

    def __unicode__(self):
        return self.name

    def was_found(self):
        return k100() <= self.visibility

    @property
    def hours_for_activity(self):
        base_hours = 4

        if self.amount_of_water_stored > 0:
            base_hours += 2
        if self.amount_of_food_stored > 0:
            base_hours += 2

        if self.has_food_utensils:
            base_hours += 1
        if self.has_clean_clothes:
            base_hours += 1
        if self.has_real_beds:
            base_hours += 1
        if self.has_storage:
            base_hours += 1

        return base_hours

    def remove_day_of_resources(self):
        errors = []

        if self.amount_of_water_stored <= 0:
            errors.append(u"Brak wody w obozie!")
            self.amount_of_water_stored = 0
        if self.amount_of_food_stored <= 0:
            errors.append(u"Brak jedzenia w obozie!")
            self.amount_of_food_stored = 0

        if errors:
            return 0, 0, errors

        removed_water = self.daily_usage_of_water
        removed_food = self.daily_usage_of_food

        if removed_water > self.amount_of_water_stored:
            missing_water = removed_water - self.amount_of_water_stored
            errors.append(u"Do zaspokojenia pragnienia zabrakło {} litrów wody!".format(missing_water))
            self.amount_of_water_stored = 0
            removed_water -= missing_water
        if removed_food > self.amount_of_food_stored:
            missing_food = removed_food - self.amount_of_food_stored
            errors.append(u"Do zaspokojenia głody zabrakło {} jednostek jedzenia!".format(missing_food))
            self.amount_of_food_stored = 0
            removed_food -= missing_food

        if not errors:
            self.amount_of_food_stored -= removed_food
            self.amount_of_water_stored -= removed_water

        return removed_water, removed_food, errors

    @property
    def daily_usage_of_water(self):
        return sum([camper.amount_of_water_needed for camper in self.campers.all()])

    @property
    def daily_usage_of_food(self):
        return sum([camper.amount_of_food_needed for camper in self.campers.all()])


class DayPassedLog(models.Model):

    camp = models.ForeignKey(Camp)

    was_found_that_day = models.BooleanField()

    water_used = models.DecimalField(
        verbose_name=u"Jednostki zużytej wody",
        decimal_places=2,
        max_digits=8
    )

    food_used = models.DecimalField(
        verbose_name=u"Jednostki zużytego jedzenia",
        decimal_places=2,
        max_digits=8
    )

    def __unicode__(self):
        if self.pk:
            return u'Day {} at {}'.format(self.pk, self.camp.name)
        else:
            return 'New day'
