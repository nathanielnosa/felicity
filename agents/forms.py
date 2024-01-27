from django import forms

from . models import Agent

class UserProfile(forms.ModelForm):
    username = forms.CharField(label=('Username'),widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Agent
        fields = ['name','username','email','password1','password2']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Full name e.g John Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Valid email e.g JohnDoe@gmail.com'}),
        }
 

class Editprofile(forms.ModelForm):
  class Meta:
    model = Agent
    fields = ['name','description', 'phone', 'mobile', 'email', 'facebook', 'instagram','twitter', 'linkedin', 'photo_main',]
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'phone': forms.TextInput(attrs={'class': 'form-control'}),
        'mobile': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram': forms.TextInput(attrs={'class': 'form-control'}),
        'twitter': forms.TextInput(attrs={'class': 'form-control'}),
        'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
        'photo_main': forms.FileInput(attrs={'class': 'form-control'}),
    }



# class SendMessage(ModelForm):
#   class Meta:
#     model = Message
#     fields = ['name','email','subject','body']
#     widgets = {
#       'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g Nathaniel Nosa'}),
#       'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'e.g NathanielNosa@gmail.com'}),
#       'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g Lookin For A Developer'}),
#       'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'e.g I need a web dev...'}),
#     }