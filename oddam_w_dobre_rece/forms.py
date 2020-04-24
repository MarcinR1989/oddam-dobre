from django import forms
from django.contrib.auth.models import User

from oddam_w_dobre_rece.models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
        }


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password1'] != cd['password2']:
        raise forms.ValidationError('Passwords are not identical')
    return cd['password2']
