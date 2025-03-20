from rest_framework import generics, status
from rest_framework.views import APIView, Response
import os
from django.core.files import File

from api.models import Category, Product
from api.serializers import ProductSerializer

class ProductsView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def get(self, request, brand='', *args, **kwargs):
    qs = self.queryset.filter(brand=brand)
    serializer = self.serializer_class(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class WorkerView(APIView):
  def get(self, request, *args, **kwargs):
    for p in Product.objects.all():
      p.name_ro = p.name_en
      p.save()
    return Response()
  
  def parse_images(self):
    folder_path = r'C:\Users\User\Coding\Python\Django\kappa\files'
    for dir in os.listdir(folder_path):
      nested_path = os.path.join(folder_path, dir)
      if os.path.isdir(nested_path):
        for filename in os.listdir(nested_path):
          file_path = os.path.join(nested_path, filename)
          print(filename, file_path)
          with open(file_path, 'rb') as f:
            django_file = File(f, name=f'{dir} {filename}')
            qs = Category.objects.filter(name_en=dir)
            if qs.exists():
              category = qs.first()
            else:
              category = Category.objects.create(name_en=dir, name_ro=dir)
              
            Product.objects.create(brand='GL', category=category, name=filename, image=django_file)
    return Response()