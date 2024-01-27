from .models import *
from django.forms import ModelForm
from django import forms

class CreateListing(forms.ModelForm):
  class Meta:
    model = Listing
    fields = ['title', 'description','price','bedrooms','bathrooms','toilets','garage','sqft','lot_size','category','listing_type','address','city','state','zipcode','furnish','photo_main','photo_1','photo_2','photo_3','photo_4','photo_5','photo_6','photo_7','photo_8','photo_9']
    widgets={
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class':'form-control'}),
      'price': forms.TextInput(attrs={'class': 'form-control'}),
      'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
      'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
      'toilets': forms.TextInput(attrs={'class': 'form-control'}),
      'garage': forms.TextInput(attrs={'class': 'form-control'}),
      'sqft': forms.TextInput(attrs={'class': 'form-control'}),
      'lot_size': forms.TextInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
      'listing_type': forms.Select(attrs={'class': 'form-control'}),
      'address': forms.TextInput(attrs={'class': 'form-control'}),
      'city': forms.TextInput(attrs={'class': 'form-control'}),
      'state': forms.TextInput(attrs={'class': 'form-control'}),
      'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
      'furnish': forms.Select(attrs={'class': 'form-control'}),
      'photo_main':forms.FileInput(attrs={'class':'form-control'}),
      'photo_1':forms.FileInput(attrs={'class':'form-control'}),
      'photo_2':forms.FileInput(attrs={'class':'form-control'}),
      'photo_3':forms.FileInput(attrs={'class':'form-control'}),
      'photo_4':forms.FileInput(attrs={'class':'form-control'}),
      'photo_5':forms.FileInput(attrs={'class':'form-control'}),
      'photo_6':forms.FileInput(attrs={'class':'form-control'}),
      'photo_7':forms.FileInput(attrs={'class':'form-control'}),
      'photo_8':forms.FileInput(attrs={'class':'form-control'}),
      'photo_9':forms.FileInput(attrs={'class':'form-control'}),
    }

