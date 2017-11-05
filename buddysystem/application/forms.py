from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

GENDER_CHOICES= [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
    ]

LOC_CHOICES= [
    ('Clark', 'Clark'),
    ('Alderman', 'Alderman'),
    ('Thornton Stacks', 'Thornton Stacks')
    ]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gender = forms.CharField(label='Gender:', widget=forms.Select(choices=GENDER_CHOICES))
    password1 = forms.CharField(label='Password', max_length=254, widget=forms.PasswordInput,
                                help_text='Your password can\'t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can\'t be a commonly used password. Your password can\'t be entirely numeric.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'gender')

class ReadyForm(forms.ModelForm):
    dep_location = forms.CharField(label='Departure location', widget=forms.Select(choices=LOC_CHOICES))
    num_companions = forms.IntegerField(label='Desired number of companions')
    destination = forms.CharField(label='Departure location', widget=forms.Select(choices=LOC_CHOICES))

    class Meta:
        model = User
        fields = ('dep_location', 'num_companions', 'destination')
