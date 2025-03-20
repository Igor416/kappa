from django.db import models
from uuid import uuid4

# Create your models here.
class Category(models.Model):
  id = models.UUIDField('id', primary_key=True, default=uuid4)
  name_en = models.CharField('Название категории (en)', max_length=32)
  name_ro = models.CharField('Название категории (ro)', max_length=32)
  
  def __str__(self):
    return self.name_en
  
  class Meta:
    ordering = ['name_en']
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

class Product(models.Model):
  BRANDS = {
    'MA': 'Maestro',
    'AP': 'Apriori',
    'TE': 'Tezaur',
    'RO': 'Roua Moldovei',
    'JA': 'J\'Adore',
    'GL': 'Glenwood',
    'TA': 'Taiga'
  }
  
  id = models.UUIDField('id', primary_key=True, default=uuid4)
  brand = models.CharField('Бренд', choices=BRANDS, max_length=2)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Категория')
  name_en = models.CharField('Название (en)', max_length=32)
  name_ro = models.CharField('Название (ro)', max_length=32)
  image = models.ImageField('Фотография', upload_to='products/')
  
  def __str__(self):
    return f'{self.get_brand_display()} {self.name}'
  
  class Meta:
    ordering = ['brand', 'category', 'name_en']
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'