from django.contrib import admin

from api.models import Category, Product

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_filter = ['brand', 'category']