from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {'username': _('Придумайте логин'), }
        help_texts = {'username': _(''), 'email': _('вводите действительный адресс для подтверждения регистрации'), }

    def clean_password2(self):   # todo (усилить пароль)
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        elif len(data['password']) < 8:
            raise forms.ValidationError('Пароль должен содержать не менее 8 символов и иметь хотя бы один символ')
        elif data['password'].isdigit():
            raise forms.ValidationError('Пароль должен содержать хотя бы один символ')

        return data['password2']
