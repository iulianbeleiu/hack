from django.contrib import admin
from .models import Unemployed, UnemployedJob


@admin.register(Unemployed)
class UnemployedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'email', 'phoneNumber', 'cv', 'itmDocuments')
    list_editable = ('name', 'email')
    list_filter = ('name', 'address', 'email', 'phoneNumber')
    search_fields = ('name', 'address')
    list_per_page = 10


@admin.register(UnemployedJob)
class UnemployedJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'unemployed', 'job')
    list_editable = ('unemployed', 'job')
    list_filter = ('unemployed', 'job')
    search_fields = ('unemployed', 'job')
    list_per_page = 10
