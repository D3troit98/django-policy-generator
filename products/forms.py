from datetime import datetime
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Input


class ProductForm(forms.Form):
        header = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Header"}))
        policy_effective_date = forms.DateField(widget=forms.TextInput(attrs={"placeholder":datetime.now}))
        website_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Website Name"}))
        application_name = forms.CharField(required=False,widget=forms.TextInput(attrs={"placeholder":"The Application name"}))
        website_url = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"www.website.com"}))
        company_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Company name"}))
        company_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"the address to your business"}))
        country_based = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Nigeria"}))
        email_address = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"eamil@gmail.com"}))


class LoginForm(forms.Form):
    email_address = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"eamil@gmail.com"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"your password"}))


class RegistrationForm(UserCreationForm):
    email  = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['header','website_name','application_name','website_url','company_name',
                    'company_address','country_based','email_address']

class SelectForm(forms.ModelForm):
    class Meta:
         model = Input
         fields = ['input']