from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import UserProfile

class NewRegForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'description',
            'city',
            'website',
            'phone',
            'image',
        )

    # def save(self, commit=True):
    #     user = super(NewRegForm, self).save(commit=False)
    #     user.description = self.cleaned_data['description']
    #     user.city = self.cleaned_data['city']
    #     user.website = self.cleaned_data['website']
    #     user.phone = self.cleaned_data['phone']
    #
    #
    #     if commit:
    #         user.save()
    #
    #     return user

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Email'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Ник'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите здесь фамилию'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user



class EditProfileForm(UserChangeForm):
    template_name='/something/else'
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Email'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите подтвердить'
        }
    ))
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
