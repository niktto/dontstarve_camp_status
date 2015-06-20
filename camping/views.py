# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages

from .models import Camp


class CampTemplateView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        camp = Camp.objects.all()[:1][0]
        return {
            'camp': camp,
            'campers': list(camp.campers.all())
        }


def pass_day_view(request):
    if not request.user.is_superuser:
        messages.add_message(request, messages.WARNING, u"Nie jesteś adminem, nie oszukuj.")
        return redirect('/')

    camp = Camp.objects.all()[:1][0]
    camp.remove_day_of_resources()

    if camp.was_found():
        messages.add_message(request, messages.WARNING, u"Obóz został odkryty!")
    else:
        messages.add_message(request, messages.INFO, u"Obóz jest bezpieczny.")

    camp.save()
    return redirect('/')
