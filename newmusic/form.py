from django import forms
from .models import Files


class UploadForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите название песни...'
        }
    ))

    artist = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя исполнителя...'
        }
    ))

    class Meta:
        model = Files
        fields = (
            'text',
            'artist',
            'our_file',
            'image',
        )
