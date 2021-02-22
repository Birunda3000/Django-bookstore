from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Compra

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('age','first_name',)

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('age',)

class CompraForm (ModelForm):
    class Meta:
        model = Compra
        fields = ('metodo_de_pagamento',)