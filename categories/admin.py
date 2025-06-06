from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
