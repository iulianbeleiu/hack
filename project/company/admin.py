from django.contrib import admin
from .models import Company, Product, Revenue
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'company')
    list_editable = ('name', 'price')
    list_filter = ('name', 'description', 'price', 'company')
    search_fields = ('name', 'description')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'activityDomain', 'email', 'phoneNumber')
    list_filter = ('name', 'address', 'activityDomain')
    search_fields = ('name', 'activityDomain')


@admin.register(Revenue)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'intervalMin', 'intervalMax', 'percent')
    list_filter = ('name', 'intervalMin', 'intervalMax', 'percent')
    search_fields = ('name', 'intervalMin', 'intervalMax', 'percent')