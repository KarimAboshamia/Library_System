from django import forms
from django.db import models
from django.db.models import fields
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['ISBN', 'name', 'publication_year', 'author_name', 'type', 'img', 'counter']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'college', 'phone']

