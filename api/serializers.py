from rest_framework.serializers import ModelSerializer

from api.models import Category, Product

class TranslatableSerializer(ModelSerializer):
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['name'] = {
      'en': r.pop('name_en'),
      'ro': r.pop('name_ro')
    }
    return r

class CategorySerializer(TranslatableSerializer):
  class Meta:
    fields = '__all__'
    model = Category

class ProductSerializer(TranslatableSerializer):
  category = CategorySerializer()
  
  class Meta:
    fields = '__all__'
    model = Product