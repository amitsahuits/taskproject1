from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm, UsernameField)
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField( label=_("Password"),
                                strip=False ,
                                widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}

        # it is not possible write classes in signup.html for form., that is why we're writing from here
        #we are doing it , so that we can add bootstrap classes in form
        widgets = {'username':forms.TextInput(attrs=
        {'class':'form-control'}),
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserEditForm(UserChangeForm):
    password : forms.TextInput(attrs={'class' : 'd-none'})
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']
        widgets = {'username':forms.TextInput(attrs=
        {'class':'form-control'}),
        
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
