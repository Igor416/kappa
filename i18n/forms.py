import json
import os
from django import forms
from django.conf import settings

LOCALES_PATH = os.path.join(settings.BASE_DIR, 'public', 'locales')

class TranslationForm(forms.Form):
  ns = forms.CharField(label='Страница', max_length=100)
  content_en = forms.CharField(widget=forms.Textarea, label='Контент (en)')
  content_ro = forms.CharField(widget=forms.Textarea, label='Контент (ro)')

  @staticmethod
  def get_namespaces():
    return os.listdir(LOCALES_PATH)
  
  @staticmethod
  def get_default_data(ns):
    data = {'en': '', 'ro': ''}
    for lang in data.keys():
      file_path = os.path.join(LOCALES_PATH, ns, f'{lang}.json')
      with open(file_path, 'r', encoding='utf-8') as f:
        data[lang] = json.dumps(json.load(f), indent=2, ensure_ascii=False)
    return {
      'ns': ns,
      'content_en': data['en'],
      'content_ro': data['ro'],
    }

  def clean_content(self, lang):
    content = self.cleaned_data['content_' + lang]
    try:
      json.loads(content)
    except json.JSONDecodeError:
      raise forms.ValidationError('Неверно форматирован текст')
    return content

  def clean_content_en(self):
    return self.clean_content('en')

  def clean_content_ro(self):
    return self.clean_content('ro')

  def load_data(self, ns, language):
    file_path = os.path.join(LOCALES_PATH, ns, f'{language}.json')
    if os.path.exists(file_path):
      with open(file_path, 'r', encoding='utf-8') as f:
        self.fields['content'].initial = json.dumps(json.load(f), indent=2, ensure_ascii=False)

  def save_data(self):
    ns = self.cleaned_data['ns']
    for lang in ['en', 'ro']:
      content = self.cleaned_data['content_' + lang]
      file_path = os.path.join(LOCALES_PATH, ns, f'{lang}.json')

      os.makedirs(os.path.dirname(file_path), exist_ok=True)
      with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json.loads(content), f, indent=2, ensure_ascii=False)
