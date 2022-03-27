from django import forms
from django.contrib.auth.models import User
from artyParty.models import UserProfile, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'review',)