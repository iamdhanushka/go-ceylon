from dataclasses import fields
from django  import forms
from catalogue.models import Review, RATE_CHOICES, OCRImage
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username','password1','password2')

class RateForm(forms.ModelForm):
    text= forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}), required=True)
    rate=forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        fields = ('text', 'rate')

class UserImage(forms.ModelForm):  
    user_img= forms.ImageField(widget=forms.FileInput(attrs={'class':'image-input'}), required=True)
    class Meta:  
        model = OCRImage
        fields = '__all__'  