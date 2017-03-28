# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from model.models import Club, UserProfile, Comment
from django.utils import timezone


class ClubFilterForm(forms.Form):
	club_title = forms.CharField(label="Место проведения", required=False)

class EventFilterForm(forms.Form):
	event_title = forms.CharField(label="Место проведения", required=False)

class CommentForm(forms.ModelForm):
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
