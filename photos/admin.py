from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from .forms import PhotosForm

class PhotosAdminPanel(admin.AdminSite):
  site_header = 'Photos Editor'

  def get_urls(self):
    urls = super().get_urls()
    custom_urls = [
      path('', self.admin_view(self.replace_photo), name='replace-photo'),
    ]
    return custom_urls + urls

  def replace_photo(self, request):
    choices = PhotosForm.get_choices()
    if request.method == 'POST':
      form = PhotosForm(request.POST, request.FILES)
      if form.is_valid():
        form.save_photo()
        messages.success(request, 'Фото изменено')
        return redirect('/admin-photos/')
    else:
      form = PhotosForm()

    return render(request, 'admin/replace_photo.html', {'form': form, 'choices': choices})

# Register the custom admin panel
admin_photos = PhotosAdminPanel(name='photos_admin')
