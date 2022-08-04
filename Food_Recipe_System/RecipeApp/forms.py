from cProfile import label
from pyexpat import model
from unittest import mock
from .models import AllRecipes
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class AddRecipe(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Your Name')
    userphone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Mobile No')
    recipe_title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    recipe=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':6}))

    class Meta:
        model=AllRecipes
        fields=['username','userphone','recipe_title','recipe']
       

class signupform(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='New Password')

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='Re-Type Password')


    class Meta:
        model=User
        fields=['username','email']

        widgets={
                'username':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                }



class signinform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
   