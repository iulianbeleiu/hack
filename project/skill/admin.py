from django.contrib import admin
from .models import Skill, SkillMatrix


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 10


@admin.register(SkillMatrix)
class SkillMatrixAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'unemployed', 'grade')
    list_editable = ('skill', 'unemployed', 'grade')
    list_filter = ('skill', 'unemployed', 'grade')
    search_fields = ('skill', 'unemployed', 'grade')
    list_per_page = 10