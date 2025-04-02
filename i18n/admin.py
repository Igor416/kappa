from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from .forms import TranslationForm

class TranslationAdminPanel(admin.AdminSite):
  site_header = 'Translation Editor'

  def get_urls(self):
    urls = super().get_urls()
    custom_urls = [
      path('', self.admin_view(self.list_translations), name='list_translations'),
      path('edit/<str:ns>/', self.admin_view(self.edit_translation), name='edit_translation'),
    ]
    return custom_urls + urls
  
  def list_translations(self, request):
    namespaces = TranslationForm.get_namespaces()
    return render(request, 'admin/translations_list.html', {'namespaces': namespaces})

  def edit_translation(self, request, ns):
    if request.method == 'POST':
      form = TranslationForm(request.POST)
      if form.is_valid():
        form.save_data()
        messages.success(request, 'Перевод изменен')
        return redirect('/admin-i18n/')
    else:
      initial_data = TranslationForm.get_default_data(ns)
      form = TranslationForm(initial=initial_data)

    return render(request, 'admin/edit_translation.html', {'form': form, 'ns': ns})

# Register the custom admin panel
admin_i18n = TranslationAdminPanel(name='translation_admin')
