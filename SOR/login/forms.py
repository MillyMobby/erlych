from django import forms
from django.contrib.auth.forms import (AuthenticationForm)

from .models import Account
#i field dei form di django risultano come campi di input nei file HTML

class SignIn(AuthenticationForm):

    username = forms.CharField(min_length=3, max_length=50, help_text='Required')
    password = forms.CharField( widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        

class Register(forms.ModelForm):
     username = forms.CharField(min_length=4, max_length=50, help_text='Required')
     email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'tentare con un altro indirizzo email'})
     password = forms.CharField(widget=forms.PasswordInput)
     password2 = forms.CharField( widget=forms.PasswordInput)

     class Meta:
          model = Account
          fields = ('username', 'email',)

     def check_if_valid_username(self):
          username = self.cleaned_data['username'].lower()
          r = Account.objects.filter(username=username)
          if r.count():
               raise forms.ValidationError("User già esiste")
          return username
     
     def clean_email(self):
        input = self.cleaned_data['email']
        if Account.objects.filter(email=input).exists():
            raise forms.ValidationError(
                'La mail utilizzata già esiste per un altro account')
        return input
     
     def clean_password2(self):
        password = self.cleaned_data
        if password['password'] != password['password2']:
            raise forms.ValidationError('Le password non corrispondono')
        return password['password2']
     
     
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


     