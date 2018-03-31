from django import forms
from home.models import GlMsg, Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Напишите сообщение...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

class HomeForm2(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Напишите сообщение...'
        }
    ))

    class Meta:
        model = GlMsg
        fields = ('post',)



