from django.db import models
from uuid import uuid4

# Create your models here.
class Brand(models.Model):
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
  name = models.CharField('Название', choices=BRANDS, max_length=2)
  
  def __str__(self):
    return self.get_name_display()
  
  class Meta:
    verbose_name = 'Бренд'
    verbose_name_plural = 'Бренды'

class Category(models.Model):
  id = models.UUIDField('id', primary_key=True, default=uuid4)
  brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Бренд')
  name_en = models.CharField('Название категории (en)', max_length=32)
  name_ro = models.CharField('Название категории (ro)', max_length=32)
  order = models.SmallIntegerField('Порядок', default=1)
  
  def __str__(self):
    return f'{self.brand} {self.name_en} ({self.order})'
  
  class Meta:
    ordering = ['brand', 'order']
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'

class Product(models.Model):
  id = models.UUIDField('id', primary_key=True, default=uuid4)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True, verbose_name='Категория')
  name_en = models.CharField('Название (en)', max_length=32)
  name_ro = models.CharField('Название (ro)', max_length=32)
  image = models.ImageField('Фотография', upload_to='products/')
  order = models.SmallIntegerField('Порядок', default=1)
  
  def __str__(self):
    return f'{self.category.brand} {self.name_en} ({self.order})'
  
  class Meta:
    ordering = ['category', 'order']
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'