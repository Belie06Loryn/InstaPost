from .models import Foto,Profile,Comment,Follower
from django import forms

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','name','username','email','bio']

class PostForm(forms.ModelForm):
  class Meta:
    model = Foto
    fields = ['image', 'caption']
  