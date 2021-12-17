from django.contrib import admin
from .models import Product, Stock, StockProduct

class ProductAdmin(admin.ModelAdmin):
    pass

class StockAdmin(admin.ModelAdmin):
    pass

class StockProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockProduct, StockProductAdmin)
