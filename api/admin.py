from django.contrib import admin

from api.models import Brand, Category, Product

admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_filter = ['brand']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_filter = ['category', 'category__brand']