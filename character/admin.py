from django.contrib import admin

from .models import CharacterSheet, Wound, Skill


class SkillInline(admin.TabularInline):

    model = Skill


class WoundInline(admin.TabularInline):

    model = Wound


class CharacterAdmin(admin.ModelAdmin):

    model = CharacterSheet
    inlines = [SkillInline, WoundInline]


admin.site.register(CharacterSheet, CharacterAdmin)
