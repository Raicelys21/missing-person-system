from django import forms
from .models import Gallery
from .models import Identify

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        labels = {'photo':' Image'}

class IdentifyForm(forms.ModelForm):
    class Meta:
        model = Identify
        fields = '__all__'
        labels = {'photo':' Image'}