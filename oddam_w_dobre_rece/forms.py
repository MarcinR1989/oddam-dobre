from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from oddam_w_dobre_rece.models import *


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
            'username': forms.TextInput(attrs={'placeholder': 'Email'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are not identical')
        return cd['password2']


class MyAuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'placeholder': 'Hasło'}),
    )


class DonationForm1(forms.ModelForm):
    name = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Category
        fields = ('name',)
        # widgets = {'name': forms.ModelMultipleChoiceField(queryset=Category.objects.all())}


class DonationForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Category.objects.all()
    # )
    # institution = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Institution.objects.all()
    # )

    class Meta:
        model = Donation
        fields = '__all__'
        # exclude = ['categories', 'institution', ]
        # fields = ('quantity', 'address', 'phone_number', 'city', 'zip_code',
        #           'pick_up_date', 'pick_up_time', 'pick_up_comment', )
        # widgets = {'categories': forms.CheckboxSelectMultiple(queryset)}


# problems = forms.ModelMultipleChoiceField(
#     widget=forms.CheckboxSelectMultiple,
#     queryset=Problem.objects.all()
# )
