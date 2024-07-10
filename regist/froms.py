import re

from django import forms
from .models import User
from django.core.exceptions import ValidationError
from datetime import timedelta, date


class UserForm(forms.Form):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control input-group'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        pattern = r'^[a-z]{3,}[0-9]{2}$'
        if not re.match(pattern, username):
            raise forms.ValidationError(
                'Kamida 5 ta belgi bolsin, Kichik harflardan iborat bolsin. Oxirgi ikkita belgisi raqamlardan iborat bolsin.')
        return username

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.endswith('.png'):
                raise forms.ValidationError('Kechirasiz rasm .png format da bolishi kerak.')
            return image

    def clean_password(self):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
        password = self.cleaned_data.get('password')
        if not re.match(pattern, password):
            raise ValidationError('Parolda kamida bir belgi (!@#$%^&*()_+-=[]{}|;\':",./<>?) bo\'lishi kerak')
        return password

    def clean_birthdate(self):
        birthday = self.cleaned_data.get('birthdate')
        if not isinstance(birthday, date):
            raise ValidationError('Noto\'g\'ri sana formati.')

        today = date.today()
        twelve_years_ago = today - timedelta(days=12 * 365)
        if birthday > twelve_years_ago:
            raise ValidationError('Ro\'yxatdan o\'tish uchun kamida 12 yoshda bo\'lishingiz kerak.')
        return birthday

    def save(self, commit=True):

        user = User(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            image=self.cleaned_data['image'],
            birthdate=self.cleaned_data['birthdate'],
        )
        if commit:
            user.save()
        return user
