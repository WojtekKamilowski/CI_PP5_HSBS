from django.contrib import admin
from .models import Book, Era

# Register your models here.

# Inspired by Code Institue's "Boutique Ado" Walkthrough Project


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'era',
        'price',
        'rating',
        'image',
        'author',
        'published',
    )

    ordering = ('sku',)


class EraAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Era, EraAdmin)
