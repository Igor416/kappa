from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('<str:arg1>', views.index),
  path('<str:arg1>/<str:arg2>', views.index),
]