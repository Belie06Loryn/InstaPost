from .models import Foto,Profile,Comment,Follower
from django import forms

class ProfileForm(forms.Form):
    image = forms.FileField()
    name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    bio = forms.CharField(max_length=6000)
