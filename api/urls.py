from django.urls import path
from . import views

urlpatterns = [
  path('products/<str:brand>/', view=views.ProductsView.as_view()),
  path('worker/', view=views.WorkerView.as_view())
]