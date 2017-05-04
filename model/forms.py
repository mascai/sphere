# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from model.models import Club, UserProfile, Comment, Like
from django.utils import timezone



class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput)



class LikeForm(forms.Form):
    model = Like
        

class ClubFilterForm(forms.Form):
	club_title = forms.CharField(label="Поиск по названию", required=False)

class EventFilterForm(forms.Form):
	event_title = forms.CharField(label="Место проведения", required=False)

class CommentForm(forms.ModelForm):
    #club = forms.CharField(widget=forms.HiddenInput)
    #club = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Comment	
        fields = ('club', 'title', 'text')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
