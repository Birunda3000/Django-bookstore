from django.contrib.auth import forms

from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('age',)

'''class CompraForm (ModelForm):
    class Meta:
        model'''