from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name', 'price', 'created_at']
    search_fields = ['brand', 'name']
