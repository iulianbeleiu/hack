from django.contrib import admin
from .models import Unemployed


@admin.register(Unemployed)
class UnemployedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'email', 'phoneNumber', 'cv', 'itmDocuments')
    list_editable = ('name', 'email')
    list_filter = ('name', 'address', 'email', 'phoneNumber')
    search_fields = ('name', 'address')
