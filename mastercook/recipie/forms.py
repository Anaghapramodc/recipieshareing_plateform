# forms.py
from django import forms


from django import forms

from .models import Profile, Recipe


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','name', 'email', 'mobile_number','image_url']
class user(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']


class recipieForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','ingredients','preparation','image_url']