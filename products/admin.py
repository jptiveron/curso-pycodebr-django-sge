from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial_number')
    search_fields = ('title', 'serial_number')


admin.site.register(Product, ProductAdmin)
