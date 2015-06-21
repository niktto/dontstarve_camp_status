# -*- coding: utf-8 -*-
from datetime import date, timedelta

from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import Camp, DayPassedLog


START_DATE = date(2030, 12, 18)


class CampListView(ListView):

    allow_empty = True
    model = Camp
    template_name = "list.html"


class CampTemplateView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        camp = get_object_or_404(Camp, uri=self.kwargs['uri'])
        today = START_DATE + timedelta(days=DayPassedLog.objects.count())
        return {
            'camp': camp,
            'today': today,
            'campers': list(camp.campers.all())
        }


def pass_day_view(request, *args, **kwargs):
    if not request.user.is_superuser:
        messages.add_message(request, messages.WARNING, u"Nie jesteś adminem, nie oszukuj.")
        return redirect('/')

    camp = get_object_or_404(Camp, uri=kwargs['uri'])
    was_found = camp.was_found()
    water_used, food_used = camp.remove_day_of_resources()

    DayPassedLog(
        camp=camp,
        was_found_that_day=was_found,
        water_used=water_used,
        food_used=food_used
    ).save()

    if was_found:
        messages.add_message(request, messages.WARNING, u"Obóz został odkryty!")
    else:
        messages.add_message(request, messages.INFO, u"Obóz jest bezpieczny.")

    camp.save()
    return redirect('/')
