from django.contrib import admin
from .models import Product, Supplier, StockTransaction

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(StockTransaction)
