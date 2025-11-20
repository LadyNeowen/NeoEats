from django.contrib import admin
from .models import MenuItem
# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'vegetarian', 'gluten_free')
    list_filter = ('category', 'vegetarian', 'gluten_free')
    search_fields = ('name', 'description')