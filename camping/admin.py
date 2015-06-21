from django.contrib import admin

from .models import Camper, Camp, DayPassedLog

# Register your models here.
admin.site.register(Camp)
admin.site.register(Camper)
admin.site.register(DayPassedLog)
