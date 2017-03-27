from django import forms
from django.contrib.auth.models import User
from model.models import Club, UserProfile, Comment

class CommentForm(forms.ModelForm):
	#club = forms.ModelChoiceField(queryset=Club.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Comment	
        fields = ('club', 'title', 'text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
