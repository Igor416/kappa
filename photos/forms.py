import os
from django import forms
from django.conf import settings

STATIC_IMAGES_PATH = os.path.join(settings.BASE_DIR, 'static', 'assets')

class PhotosForm(forms.Form):
  photo_name = forms.CharField(label='фото')
  new_photo = forms.ImageField(label='Новое фото')

  @staticmethod
  def get_choices():
    choices = []
    for root, _, files in os.walk(STATIC_IMAGES_PATH):
      for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
          relative_path = os.path.relpath(os.path.join(root, file), STATIC_IMAGES_PATH)
          choices.append(relative_path)

    return choices

  def save_photo(self):
    photo_name = self.cleaned_data['photo_name']
    new_photo = self.cleaned_data['new_photo']
    file_path = os.path.join(STATIC_IMAGES_PATH, photo_name)

    # Overwrite existing file with new photo
    with open(file_path, 'wb') as f:
      for chunk in new_photo.chunks():
        f.write(chunk)
